import json
from kafka import KafkaProducer
from kafka import KafkaConsumer



ORDERED_KAFKA_TOPIC = "order_details"
ORDERED_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(ORDERED_KAFKA_TOPIC, bootstrap_servers="localhost:29092")
producer = KafkaProducer(bootstrap_servers="localhost:29092")
print("Gonna start listening")

while True:
    for message in consumer:
        print("ongoing transaction")
        consumed_message = json.loads(message.value.decode())
        print(consumed_message)
        user_id = consumed_message["user_id"]
        total_cost = consumed_message["total_cost"]
        data = {
            "customer_id": user_id,
            "customer_email": f"{user_id}@gmail.com",
            "total_cost": total_cost,

        }

        print("successful transaction")
        producer.send(ORDERED_CONFIRMED_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))


