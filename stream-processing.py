import argparse
import atexit
import json
import logging
import time

from kafka import KafkaProducer
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

logging.basicConfig()
logger = logging.getLogger("stream-processing")
logger.setLevel(logging.INFO)

kafka_producer = None
topic = None
kafka_broker = None
new_topic = None

def shutdown_hook(producer):
	logger.info('Prepare to shut down producer')
	producer.flush(10)
	producer.close(10)

def process(timeobject, rdd):
	# logger.info(rdd)
	num_of_records = rdd.count()
	if num_of_records == 0:
		return

	price_sum = rdd.map(lambda record : float(json.loads(record[1].decode('utf-8'))[0].get('LastTradePrice'))).reduce(lambda a, b : a + b)
	average = price_sum / num_of_records
	logger.info('Received %d records from kafka, average price is %f' % (num_of_records, average))

	current_time = time.time()
	data = json.dumps({
		'timestamp': current_time,
		'average': average
	})

	try:
		kafka_producer.send(new_topic, value=data)
	except Exception:
		logger.warn('Fail to send data')

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('kafka_broker', help='location of kafka')
	parser.add_argument('topic', help='original topic name')
	parser.add_argument('new_topic', help='new topic to send data to')

	args = parser.parse_args()
	kafka_broker = args.kafka_broker
	topic = args.topic
	new_topic = args.new_topic

	kafka_producer = KafkaProducer(bootstrap_servers=kafka_broker)

	sc = SparkContext("local[2]", "StockAveragePrice")
	sc.setLogLevel('ERROR')
	ssc = StreamingContext(sc, 5)

	kafkaStream = KafkaUtils.createDirectStream(ssc, [topic], {'metadata.broker.list': kafka_broker})
	kafkaStream.foreachRDD(process)

	atexit.register(shutdown_hook, kafka_producer)

	ssc.start()
	ssc.awaitTermination()