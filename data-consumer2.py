# - consume data from a new kafka topic, which has been processed by spark streaming

from kafka import KafkaConsumer
consumer = KafkaConsumer('average-stock-price', bootstrap_servers='192.168.99.100:9092')
for msg in consumer:
    print(msg)
