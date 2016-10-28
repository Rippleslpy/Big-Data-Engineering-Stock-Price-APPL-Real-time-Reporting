#data-storage.py
#-- read from specific  kafka cluster & topic
#-- write to cassandra cluster 
#-- data need to be organized according to sstable
#-- no flask required, no configure change while running
from kafka import KafkaConsumer
from cassandra.cluster import Cluster

import argparse
import logging
import json
import atexit


# - default kafka topic to read from
topic_name = 'stock-analyzer'

# - default kafka broker location
kafka_broker = '127.0.0.1:9092'

# - default cassandra nodes to connect
cassandra_broker = '192.168.99.100'

# - default keyspace to use
key_space = 'stock'

# - default table to use
data_table = 'stock'


logger_format = '%(asctime)-15s %(message)s'
logging.basicConfig(format=logger_format)
logger = logging.getLogger('data-storage')
logger.setLevel(logging.DEBUG)

def persist_data(stock_data, cassandra_session):
	#ConsumerRecord(topic=u'stock-analyzer', partition=0, offset=571, timestamp=1477571443514L, timestamp_type=0, key=None, value='[{"Index": "NYSE", "LastTradeWithCurrency": "43.37", "LastTradeDateTime": "2016-10-26T16:02:23Z", "LastTradePrice": "43.37", "LastTradeTime": "4:02PM EDT", "LastTradeDateTimeLong": "Oct 26, 4:02PM EDT", "StockSymbol": "A", "ID": "663860"}, {"Index": "NYSE", "LastTradeWithCurrency": "73.83", "LastTradeDateTime": "2016-10-26T16:02:03Z", "LastTradePrice": "73.83", "LastTradeTime": "4:02PM EDT", "LastTradeDateTimeLong": "Oct 26, 4:02PM EDT", "StockSymbol": "D", "ID": "10020"}, {"Index": "NYSE", "LastTradeWithCurrency": "6.36", "LastTradeDateTime": "2016-10-26T16:02:41Z", "LastTradePrice": "6.36", "LastTradeTime": "4:02PM EDT", "LastTradeDateTimeLong": "Oct 26, 4:02PM EDT", "StockSymbol": "S", "ID": "451755032207425"}, {"Index": "NYSE", "LastTradeWithCurrency": "74.07", "LastTradeDateTime": "2016-10-26T16:01:17Z", "LastTradePrice": "74.07", "LastTradeTime": "4:01PM EDT", "LastTradeDateTimeLong": "Oct 26, 4:01PM EDT", "StockSymbol": "K", "ID": "20562"}]', checksum=1134172970, serialized_key_size=-1, serialized_value_size=961)
	logger.debug('Start to persist data to cassandra %s', stock_data)
	parsed = json.loads(stock_data)[0]
	symbol = parsed.get('StockSymbol')
	price = float(parsed.get('LastTradePrice'))
	trade_time = parsed.get('LastTradeDateTime')

	#CQL
	statement = "INSERT INTO %s (stock_symbol, trade_time, trade_price) VALUES ('%s', '%s', %f)" % (data_table, symbol, trade_time, price)
	cassandra_session.execute(statement)
	logger.info('Persistend data to cassandra for symbol: %s, price: %f, tradetime: %s' % (symbol, price, trade_time))

def shutdown_hook(consumer, session):
	try:
		logger.info('Closing Kafka Consumer')
		consumer.close()
		logger.info('Kafka Consumer closed')
		logger.info('Closing Cassandra Session')
		session.shutdown()
		logger.info('Cassandra Session closed')
	except KafkaError as kafka_error:
		logger.warn('Failed to close Kafka Consumer, caused by: %s', kafka_error.message)
	finally:
		logger.info('Existing program')


if __name__ == '__main__':
	#set up commandline arguments
	parser = argparse.ArgumentParser()
	#help is  hint info
	parser.add_argument('topic_name', help='the kafka topic to subscribe from')
	parser.add_argument('kafka_broker', help='the location of the kafka broker')
	parser.add_argument('key_space', help='the keyspace to use in cassandra')
	parser.add_argument('data_table', help='the data table to use')
	parser.add_argument('cassandra_broker', help='the cassandra_broker location')
	
	args = parser.parse_args()
	topic_name = args.topic_name
	kafka_broker = args.kafka_broker
	key_space = args.key_space
	data_table = args.data_table
	#assume csd_broker split in ','
	cassandra_broker = args.cassandra_broker

	consumer = KafkaConsumer(topic_name,bootstrap_servers=kafka_broker)
#	 for msg in consumer:
#		print msg

	#--cassandra session
	cassandra_cluster= Cluster(contact_points=cassandra_broker.split(','))
	session = cassandra_cluster.connect()


	#-- check if keyspace was created
	#-- create keyspace if not exist
	#-- CQL, SQL-like grammar
	#replication unit is keyspace
	session.execute("CREATE KEYSPACE IF NOT EXISTS %s WITH replication = {'class': 'SimpleStrategy', 'replication_factor': '3'} AND durable_writes = 'true' " % key_space)
	session.set_keyspace(key_space) #use the created keyspace
	session.execute("CREATE TABLE IF NOT EXISTS %s (stock_symbol text , trade_time timestamp, trade_price float, PRIMARY KEY (stock_symbol, trade_time))" % data_table)
	

	atexit.register(shutdown_hook, consumer, session)

	for msg in consumer:
		persist_data(msg.value, session)
	