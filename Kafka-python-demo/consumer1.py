from kafka import KafkaConsumer
import json

consumer = KafkaConsumer("test-topic",bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    group_id='simple-group',
    value_deserializer=lambda v: json.loads(v.decode('utf-8'))
)
print(" Consumer 1 Listening")
for message in consumer:
    print(" Consumer 1 Received:", message.value)
