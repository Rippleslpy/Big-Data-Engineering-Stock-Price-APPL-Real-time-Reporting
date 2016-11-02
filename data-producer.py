import atexit
import logging
import json

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

logger.setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_envvar('ENV_CONFIG_FILE')
kafka_broker = app.config['CONFIG_KAFKA_ENDPOINT']
kafka_topic = app.config['CONFIG_KAFKA_TOPIC']

producer = KafkaProducer(bootstrap_servers=kafka_broker)

schedule = BackgroundScheduler()
schedule.add_executor('threadpool')
schedule.start()

symbols = set()

def shutdown_hook():
	logger.info('shudown kafka producer')
	producer.flush(10)
	producer.close()
	logger.info('shutdown scheduler')
	schedule.shutdown()

def fetch_price(symbol):
	try:
		logger.debug('Start to fetch stock price for %s', symbol)
		stock_price = json.dumps(getQuotes(symbol))
		#logger.debug('Retrived stock price %s', stock_price)
		producer.send(topic=kafka_topic, value=stock_price)
		logger.debug('Finish write %s price to kafka', symbol)
	except KafkaTimeoutError as timeout_error:
		logger.warn('Failed to send stock price for %s to kafka, caused by %s', (symbol, timeout_error.message))
	except Exception as e:
		logger.error('Failed to send stock price for %s', symbol)

@app.route('/', methods=['GET'])
def default():
	logger.debug('user accessed /')
	return jsonify('ok'), 200

@app.route('/<symbol>', methods=['POST'])
def add_stock(symbol):
	if not symbol:
		return jsonify({
			'error': 'Stock symbol cannot be empty'
		}), 400
	if symbol in symbols:
		pass
	else:
		symbols.add(symbol)
		schedule.add_job(fetch_price, 'interval', [symbol], seconds=1, id=symbol)
	return jsonify(list(symbols)), 200

@app.route('/<symbol>', methods=['DELETE'])
def del_stock(symbol):
	if not symbol:
		return jsonify({
			'error': 'Stock symbol cannot be empty'
		}), 400
	if symbol not in symbols:
		pass
	else:
		symbols.remove(symbol)
		schedule.remove_job(symbol)
	return jsonify(list(symbols)), 200

atexit.register(shutdown_hook)
app.run(host='0.0.0.0', port=5000)


















