from cassandra.cluster import Cluster
from kafka import KafkaConsumer
from kafka.errors import KafkaError

import argparse
import atexit
import json
import logging

logging.basicConfig()
logger = logging.getLogger('data-storage')
logger.setLevel(logging.DEBUG)

def persist_data(stock_data, cassandra_session, table):
	try:
		logger.debug('Start to persist data to cassandra %s' % stock_data)
		parsed = json.loads(stock_data)[0]
		symbol = parsed.get('StockSymbol')
		price = float(parsed.get('LastTradePrice'))
		trade_time = parsed.get('LastTradeDateTime')

		# insert to cassandra
		statement = "INSERT INTO %s (stock_symbol, trade_time, trade_price) VALUES ('%s', '%s', %f)" % (table, symbol, trade_time, price)
		cassandra_session.execute(statement)
		logger.info('Persisted data to cassandra for symbol %s, price %f, tradetime %s' % (symbol, price, trade_time))
	except Exception:
		logger.error('Failed to persist data to cassandra %s', stock_data)

def shutdown_hook(kafkaconsumer, cassandra_session):
	try:
		logger.info('Closing kafka consumer')
		consumer.close()
		logger.info('Kafka consumer closed')

		logger.info('Closing cassandra session')
		session.shutdown()
		logger.info('Cassandra session shutdown')
	except KafkaError as kafka_error:
		logger.warn('Failed to close Kafka Consumer, caused by: %s', kafka_error.message)
	finally:
		logger.info('Exiting program')

if __name__ == '__main__':
	# setup command line arg
	parser = argparse.ArgumentParser()
	parser.add_argument('topic_name', help='the Kafka topic to subscribe from')
	parser.add_argument('kafka_broker', help='the location of kafka broker')
	parser.add_argument('key_space', help='the keyspace to write data to')
	parser.add_argument('data_table', help='the data table to use')
	parser.add_argument('cassandra_broker', help='the cassandra broker location')

	args = parser.parse_args()
	topic_name = args.topic_name
	print(topic_name)
	kafka_broker = args.kafka_broker
	print(kafka_broker)
	key_space = args.key_space
	print(key_space)
	data_table = args.data_table
	print(data_table)
	cassandra_broker = args.cassandra_broker
	print(cassandra_broker)

	consumer = KafkaConsumer(
		topic_name,
		bootstrap_servers=kafka_broker
	)

	# for msg in consumer:
	# 	print(msg)

	# create cassandra session
	cassandra_cluster = Cluster(
		contact_points=cassandra_broker.split(',')	# need an array
	)
	session = cassandra_cluster.connect()

	# check if keyspace datatable is available. create if not exist
	# CQL
	session.execute(
		"CREATE KEYSPACE IF NOT EXISTS %s WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3} AND durable_writes = 'true'" % key_space
	)
	session.set_keyspace(key_space)
	session.execute(
		"CREATE TABLE IF NOT EXISTS %s (stock_symbol text, trade_time timestamp, trade_price float, PRIMARY KEY (stock_symbol, trade_time)) " % data_table
	)

	atexit.register(shutdown_hook, consumer, session)

	for msg in consumer:
		persist_data(msg.value, session, data_table)



