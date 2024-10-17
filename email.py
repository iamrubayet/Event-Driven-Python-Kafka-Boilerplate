import json

from kafka import KafkaConsumer


ORDERED_CONFIRMED_KAFKA_TOPIC = "order_confirmed"

consumer = KafkaConsumer(ORDERED_CONFIRMED_KAFKA_TOPIC, bootstrap_servers="localhost:29092")

email_sent_so_far = set()

print("Gonna start listening")

while True:
    for message in consumer:
        print("ongoing transaction")
        consumed_message = json.loads(message.value.decode())
        customer_email = consumed_message["customer_email"]
        print(f"Sending email to {customer_email}")
        email_sent_so_far.add(customer_email)
        print(f"Total emails sent so far: {len(email_sent_so_far)}")