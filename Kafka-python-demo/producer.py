from kafka import KafkaProducer
import json, time

producer = KafkaProducer( bootstrap_servers=['localhost:9092'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))

for i in range(3):
    msg = {"id": i, "text": f"Hello Kafka {i}"}
    producer.send("test-topic", value=msg)
    print("Sent:", msg)
    time.sleep(1)

producer.flush()
producer.close()
print("Messages sent")
