# - get data and write to kafka
from kafka import KafkaProducer
from apscheduler.schedulers.background import BackgroundScheduler 
from googlefinance import getQuotes
import logging
import json
from kafka.errors import (
	KafkaTimeoutError,
	KafkaError
)

from  flask import(
	Flask,
	jsonify 

)


logger_format='%(asctime)-15s %(message)s'
logging.basicConfig(format=logger_format)
logger=logging.getLogger('data-producer')
logger.setLevel(logging.DEBUG)
producer = KafkaProducer(bootstrap_servers='192.168.99.100:9092')

schedule=BackgroundScheduler()
schedule.add_executor('threadpool')
schedule.start()

app=Flask(__name__)

symbols=set()


def fetch_price(symbol):
	try:

		logger.debug('start to fetch stock price for %s',symbol)
		stock_price=json.dumps(getQuotes(symbol))
		logger.debug('Retrieved stock price %s',stock_price)
		producer.send(topic='stock-analyzer',value=stock_price)
		logger.debug('finish write %s price to kafka',symbol)
	except KafkaTimeoutError as timeout_error:
		logger.warn('Failed to send stock price for %s to kafka, caused by: %s',(symbol,timeout_error))
	except Exception as e:
		logger.error('Fialed to send stock price for %s',symbol)


#fetch_price('AAPL')

#schedule.add_job(fetch_price,'interval',['AAPL'],seconds=1,id='AAPL')


@app.route('/<symbol>',methods={'GET'})
def defualt():
	logger.debug('user access /')
	return jsonify('ok'),200


# - add stock

@app.route('/<symbol>',methods={'POST'})
def add_stock():
	if not symbol:
		return jsonify({
			'error':'Stock symbol cannot be empty'
			}), 400
	if symbol in symbols:
		pass
	else:
		symbols.add(symbol)
		schedule.add_job(fetch_price,'interval',[symbol],seconds=1,id=symbol)
	return jsonify(list(symbols)),200
	pass
# - remove stock
@app.route('/<symbol>',methods={'DELETE'})
def del_stock():
	if not symbol:
		return jsonify({
			'error':'Stock symbol cannot be empty'
			}), 400
 
	if symbol in symbols:
		pass
	else:
		#do something
		symbols.remove(symbol)
		schedule.remove_job(symbol)
	return jsonify(list(symbols)),200

app.run(host='0.0.0.0',port=5000,debug=True)