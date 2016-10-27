# - 1. read from specific kafka cluster and topic
# - 2. write to specific canssandra cluster and topic
# - 3. data need to be organized according to SSTable

from cassandra.cluster import Cluster
from kafka import KafkaConsumer

import argparse
import atexit
import logging
import json

logging.basicConfig()
logger = logging.getLogger('data-storage')
logger.setLevel(logging.INFO)

def persist_data(stock_data, cassandra_session, table):
    logger.debug('Start to persist data to cassandra %s.' % stock_data)
    parsed = json.loads(stock_data)[0]
    symbol = parsed.get('StockSymbol')
    price = float(parsed.get('LastTradePrice'))
    trade_time = parsed.get('LastTradeDateTime')
    # - insert data into cassandra
    statement = "INSERT INTO %s (stock_symbol, trade_time, trade_price) VALUES ('%s', '%s', %f)" % (table, symbol, trade_time, price)
    cassandra_session.execute(statement)
    logger.info('Persisted data to cassandra for symbol %s, price %f, tradetime %s.' % (symbol, price, trade_time))

def shutdown_hook(kafkaconsumer, cassandra_session):
    try:
        logger.info('Closing kafka consumer.')
        consumer.close()
        logger.info('Kafka consumer is closed.')
        logger.info('Closing cassandra session.')
        session.shutdown()
        logger.info('cassandra session is closed.')
    except Exception as e:
        logging.warn('Kafka consumer or cassandra session cannot be closed properly.')

if __name__ == '__main__':
    # - setup commandline arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('topic_name', help='the kafka topic to subscribe from')
    parser.add_argument('kafka_broker', help='the location of kafka broker')
    parser.add_argument('key_space', help='the keyspace to write data')
    parser.add_argument('data_table', help='the data table to use')
    parser.add_argument('cassandra_broker', help='the location of canssandra broker')

    args = parser.parse_args()
    topic_name = args.topic_name
    kafka_broker = args.kafka_broker
    key_space = args.key_space
    data_table = args.data_table
    cassandra_broker = args.cassandra_broker

    # print(args)

    # - create kafka consumer
    consumer = KafkaConsumer(
        topic_name,
        bootstrap_servers = kafka_broker

    )

    # - create cassandra session
    cassandra_cluster = Cluster(
        # - canssandra broker can be a cluster on the ring
        contact_points = cassandra_broker.split(',')
    )
    session = cassandra_cluster.connect()

    # - check whether datatable is created
    # - create keyspace if not exist
    # - CQL <= similar as SQL
    session.execute(
        "CREATE KEYSPACE IF NOT EXISTS %s WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 3} AND durable_writes = 'true'" % key_space
    )
    session.set_keyspace(key_space)
    session.execute(
        "CREATE TABLE IF NOT EXISTS %s (stock_symbol text, trade_time timestamp, trade_price float, PRIMARY KEY (stock_symbol, trade_time))" % data_table
    )

    # - setup shotdown hook
    atexit.register(shutdown_hook, consumer, session)

    for msg in consumer:
        persist_data(msg.value, session, data_table)
