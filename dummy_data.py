import pandas as pd
import random
from datetime import datetime, timedelta

stations = [
    "Central Park North",
    "Times Square",
    "Union Square",
    "Columbus Circle",
    "Madison Square",
    "Grand Central",
    "Wall Street",
    "Brooklyn Bridge",
    "Chelsea",
    "SoHo"
]

data = []

for i in range(500):

    start_station = random.choice(stations)

    end_station = random.choice(
        [s for s in stations if s != start_station]
    )

    start_time = datetime.now() - timedelta(
        minutes=random.randint(0, 1440)
    )

    duration = random.randint(5, 60)

    end_time = start_time + timedelta(
        minutes=duration
    )

    user_type = random.choice([
        "member",
        "casual"
    ])

    data.append({
        "ride_id": f"RIDE_{i+1:04d}",
        "started_at": start_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "ended_at": end_time.strftime(
            "%Y-%m-%d %H:%M:%S"
        ),
        "start_station": start_station,
        "end_station": end_station,
        "duration_minutes": duration,
        "member_casual": user_type
    })

df = pd.DataFrame(data)

df.to_csv(
    "citibike_dummy_data.csv",
    index=False
)

print("500 dummy Citi Bike records created.")
print("File: citibike_dummy_data.csv")
