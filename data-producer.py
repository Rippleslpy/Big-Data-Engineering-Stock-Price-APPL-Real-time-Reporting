# - get data and write to kafka

import logging
import json
import atexit

from apscheduler.schedulers.background import BackgroundScheduler
from flask import (
	Flask,
	jsonify
)
from googlefinance import getQuotes
from kafka import KafkaProducer
from kafka.errors import (
	KafkaTimeoutError,
	KafkaError
)

logger_format = '%(asctime)-15s %(message)s'
logging.basicConfig(format=logger_format)
logger = logging.getLogger('data-producer')

# - DEBUG INFO WARNING ERROR
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_envvar('ENV_CONFIG_FILE')
kafka_broker = app.config['CONFIG_KAFKA_ENDPOINT']
kafka_topic = app.config['CONFIG_KAFKA_TOPIC']

producer = KafkaProducer(bootstrap_servers=kafka_broker)

scheduler = BackgroundScheduler()
scheduler.add_executor('threadpool')
scheduler.start()

symbols = list()

def shutdown_hook():
	# - close kafka producer
	# - close scheduler
	logger.info('Kafka producer is shutting down.')
	producer.flush(10)
	producer.close()
	logger.info('Scheduler is shutting down.')
	scheduler.shutdown()

def fetch_price(symbol):
	try:
		logger.debug('Start to fetch stock price for %s.', symbol)
		stock_price = json.dumps(getQuotes(symbol))
		logger.debug('Retrived stock price for %s.', symbol)
		producer.send(topic=kafka_topic, value=stock_price)
		logger.debug('Finished writing stock price for %s to kafka.', symbol)
	except KafkaTimeoutError as timeout_error:
		# - retry
		logger.error('Failed to send stock price for %s to kafka, caused by: %s.', (symbol, timeout_error.message))
	except Exception as e:
		logger.error('Failed to send stock price for %s to kafka.', symbol)

# fetch_price('GOOG')

# scheduler.add_job(fetch_price, 'interval', ['AAPL'], seconds=1, id='AAPL')
# while True:
# 	pass

@app.route('/', methods=['GET'])
def default():
	logger.debug('user accessed /')
	return jsonify('OK'), 200

# - add stock
@app.route('/<symbol>', methods=['POST'])
def add_stock(symbol):
	if not symbol:
		return jsonify({
			'error': 'Stock name cannot be empty.'
			}), 400
	if symbol in symbols:
		pass
	else:
		# - do something
		symbols.append(symbol)
		scheduler.add_job(fetch_price, 'interval', [symbols], seconds=1, id=symbol)
	return jsonify(list(symbols)), 200

# - remove stock
@app.route('/<symbol>', methods=['DELETE'])
def del_stock(symbol):
	if not symbol:
		return jsonify({
			'error': 'Stock name cannot be empty.'
			}), 400
	if symbol not in symbols:
		pass
	else:
		# - do something
		symbols.remove(symbol)
		scheduler.remove_job(symbol)
	return jsonify(list(symbols)), 200

atexit.register(shutdown_hook)
app.run(host='0.0.0.0', port=5000)
