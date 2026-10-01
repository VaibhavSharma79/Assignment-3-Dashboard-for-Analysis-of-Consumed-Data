from kafka import KafkaProducer
import pandas as pd
import json
import time

KAFKA_BROKER = "localhost:9092"
TOPIC = "citibike-trips"

producer = KafkaProducer(
    bootstrap_servers=KAFKA_BROKER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

df = pd.read_csv("citibike_dummy_data.csv")

print("Producer started...")
print("Sending data to:", TOPIC)

for _, row in df.iterrows():

    data = {
        "ride_id": row["ride_id"],
        "started_at": row["started_at"],
        "ended_at": row["ended_at"],
        "start_station": row["start_station"],
        "end_station": row["end_station"],
        "duration_minutes": int(row["duration_minutes"]),
        "member_casual": row["member_casual"]
    }

    producer.send(TOPIC, value=data)

    print("Sent:", data)

    time.sleep(1)

producer.flush()
producer.close()

print("All records sent.")