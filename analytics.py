import json
from kafka import KafkaConsumer

ORDERED_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(ORDERED_CONFIRMED_KAFKA_TOPIC, bootstrap_servers="localhost:29092")


total_orders_count = 0
total_revenue = 0

print("Gonna start listening")

while True:
    for message in consumer:
        print("ongoing transaction")
        consumed_message = json.loads(message.value.decode())
        total_cost = float(consumed_message["total_cost"])
        total_orders_count += 1
        total_revenue += total_cost
        print(f"orders so far: {total_orders_count}")
        print(f"revenue so far: {total_revenue}")