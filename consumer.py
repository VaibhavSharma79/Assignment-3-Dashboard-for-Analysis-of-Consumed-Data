from kafka import KafkaConsumer
import json
import os

KAFKA_BROKER = "localhost:9092"
TOPIC = "citibike-trips"

OUTPUT_FILE = "citibike_stream.json"

consumer = KafkaConsumer(
    TOPIC,
    bootstrap_servers=KAFKA_BROKER,
    group_id="sda-assignment-3-consumer",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(
        x.decode("utf-8")
    )
)

print("Consumer started...")
print("Listening to:", TOPIC)

records = []

if os.path.exists(OUTPUT_FILE):
    try:
        with open(OUTPUT_FILE, "r", encoding="utf-8") as file:
            records = json.load(file)
    except:
        records = []

for message in consumer:

    data = message.value

    records.append(data)

    with open(
        OUTPUT_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(
            records,
            file,
            indent=4
        )

    print(
        f"Saved: {data['ride_id']} | "
        f"{data['start_station']} → "
        f"{data['end_station']}"
    )