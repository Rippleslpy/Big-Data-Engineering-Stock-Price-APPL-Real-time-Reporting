#- getdata and write to kafka
import atexit
import logging
import json
import time

from kafka import KafkaProducer
from googlefinance import getQuotes
from apscheduler.schedulers.background import BackgroundScheduler
from kafka.errors import KafkaError, KafkaTimeoutError
from flask import jsonify , Flask

# - default kafka topic to write timeout_error
topic_name = 'stock-analyzer'

# - default kafka broker location
kafka_broker = '127.0.0.1:9092'


logger_format = '%(asctime)-15s %(message)s'
logging.basicConfig(format=logger_format)
logger = logging.getLogger('data-producer')
logger.setLevel(logging.DEBUG)

#producer = KafkaProducer(bootstrap_servers='192.168.99.100:9092')


app = Flask(__name__)
app.config.from_envvar('ENV_CONFIG_FILE')
#need to create env variation
kafka_broker = app.config['CONFIG_KAFKA_ENDPOINT']
topic_name = app.config['CONFIG_KAFKA_TOPIC']

producer = KafkaProducer(bootstrap_servers=kafka_broker)
schedule = BackgroundScheduler()
schedule.add_executor('threadpool')
schedule.start()

symbols = set()
def shutdown_hook():
	#-- close kafka
	logger.info('Flushing pending messages to kafka, timeout is set to 10s')
	producer.flush(10)
	logger.info('Finish flushing pending messages to kafka')
	#-- scheduler
	schedule.shutdown()

def fetch_price(symbol):

    try:
        # price = json.dumps(getQuotes(symbol))
        logger.debug('start fetching stock price for %s', symbol)
        stock_price = json.dumps(getQuotes(symbol))
        #logger.debug('retrieved stock price %s', stock_price)
        producer.send(topic=topic_name, value=stock_price)
        logger.debug('finish writing %s price to kafka', symbol)
    except KafkaTimeoutError as timeout_error:
        logger.error('failed to send stock price for %s to kafka, caused by: %s', (symbol, timeout_error.message))
    except Exception as e:
        logger.error('failed to fetch stock price for %s', symbol)

#schedule.add_job(fetch_price, 'interval', ['AAPL'], seconds=1, id='AAPL')

@app.route('/', methods=['GET'])
def default():
	logger.debug('user accessed /')
	return jsonify('ok'), 200

#-- add stock
@app.route('/<symbol>', methods=['POST'])
def add_stock(symbol):
	if not symbol:
		return jsonify({
			'error' : 'Stock symbol cannot be empty'
			}), 400
	if symbol in symbols:
		pass
	else:
		symbols.add(symbol)
		schedule.add_job(fetch_price, 'interval', [symbol], seconds=1, id=symbol)
	return jsonify(list(symbols)), 200

#-- remove stock
@app.route('/<symbol>', methods=['DELETE'])
def del_stock(symbol):
	if not symbol:
		return jsonify({
			'error' : 'Stock symbol cannot be empty'
			}), 400
	if symbol not in symbols:
		pass
	else:
		symbols.remove(symbol)
		schedule.remove_job(symbol)
	return jsonify(list(symbols)), 200
app.run(host='0.0.0.0', port=5000, debug=True)
#if debug=True, flask can activate app whenever you change this file.

atexit.register(shutdown_hook)