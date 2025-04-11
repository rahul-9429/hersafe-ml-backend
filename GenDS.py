import pandas as pd
import random
from datetime import datetime, timedelta

# Commonly safe places in Vizag
safe_locations = [
    ("RK Beach", 17.7191, 83.3195),
    ("Kailasagiri", 17.7485, 83.3422),
    ("Rushikonda Beach", 17.7825, 83.3865),
    ("Visakha Valley School", 17.7515, 83.3636),
    ("CMR Central", 17.7399, 83.3017),
    ("City Central Park", 17.7178, 83.3124),
    ("Tenneti Park", 17.7464, 83.3513),
    ("Andhra University", 17.7306, 83.3198),
    ("Daba Gardens", 17.7099, 83.2975),
    ("Vizag Railway Station", 17.7041, 83.2936)
]

# Generate safe data
def generate_safe_data(num_records=2500):
    data = []
    for _ in range(num_records):
        location, lat, lon = random.choice(safe_locations)
        date = datetime(2023, 1, 1) + timedelta(days=random.randint(0, 364))
        time = timedelta(hours=random.randint(6, 18), minutes=random.randint(0, 59))
        date_time = (date + time).strftime('%Y-%m-%d %H:%M:%S')
        data.append({
            "date_time": date_time,
            "latitude": lat + random.uniform(-0.0005, 0.0005),
            "longitude": lon + random.uniform(-0.0005, 0.0005),
            "location": location,
            "crime_type": "none"
        })
    return pd.DataFrame(data)

# Generate and save
df = generate_safe_data()
df.to_csv("safe_data_vizag.csv", index=False)
print("✅ Dataset generated and saved.")
