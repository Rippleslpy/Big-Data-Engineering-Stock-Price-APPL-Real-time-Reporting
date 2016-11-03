# - read data from kafka
# - process data
# - send data back to kafka
# - kafka location and kafka topic

import atexit
import argparse
import logging
import json
import time

from kafka import KafkaProducer
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

logging.basicConfig()
logger = logging.getLogger('stream-processing')
logger.setLevel(logging.INFO)

kafka_producer = None
topic = None
kafka_broker = None
new_topic = None

def shutdwon_hook(producer):
	logger.info('Prepare to shut down producer.')
	producer.flush(10)
	producer.close(10)

def process(timeobject, rdd):
	# - setup log level
	# logger.info(rdd)

	# - cal average
	num_of_records = rdd.count()
	if num_of_records == 0:
		return

	price_sum = rdd.map(lambda record: float(json.loads(record[1].decode('utf-8'))[0].get('LastTradePrice'))).reduce(lambda a, b: a + b)
	average = price_sum / num_of_records
	logger.info('Received %d records from kafka, the average price is %f.' %(num_of_records, average))
	current_time = time.time()
	data = json.dumps({
		'timestamp': current_time,
		'average': average
		})

	try:
		kafka_producer.send(new_topic, value=data)
	except Exception:
		logger.warn('Fail to send data to new kakfa topic.')

if __name__ == '__main__':
	# - setup command line argument
	parser = argparse.ArgumentParser()
	parser.add_argument('kafka_broker', help='location of kafka')
	parser.add_argument('topic', help='old topic name')
	parser.add_argument('new_topic', help='new topic name')


	# - read parameters from command line
	args = parser.parse_args()
	kafka_broker = args.kafka_broker
	topic = args.topic
	new_topic = args.new_topic

	kafka_producer = KafkaProducer(bootstrap_servers=kafka_broker)

	# - setup spark streaming utilities
	sc = SparkContext("local[2]", "StockAveragePrice")
	sc.setLogLevel('ERROR')
	ssc = StreamingContext(sc, 5)

	kafkaStream = KafkaUtils.createDirectStream(ssc, [topic], {'metadata.broker.list': kafka_broker})
	kafkaStream.foreachRDD(process)

	atexit.register(shutdwon_hook, kafka_producer)

	ssc.start()
	ssc.awaitTermination()
