import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set seed
random.seed(42)
np.random.seed(42)

def generate_point(lat_range, lon_range, label, crime_type, date_range):
    date_time = datetime.strptime(random.choice(date_range), "%Y-%m-%d") + timedelta(
        hours=random.randint(0, 23), minutes=random.randint(0, 59))
    return {
        "latitude": round(random.uniform(*lat_range), 6),
        "longitude": round(random.uniform(*lon_range), 6),
        "date_time": date_time.strftime("%Y-%m-%d %H:%M:%S"),
        "crime_type": crime_type,
        "safety_level": label
    }

# Vizag range and date range
lat_range = (17.65, 17.80)
lon_range = (83.20, 83.35)
date_range = pd.date_range("2023-01-01", "2023-12-31").strftime("%Y-%m-%d").tolist()

data = []

# Safe: 850
for _ in range(850):
    data.append(generate_point(lat_range, lon_range, 0, "None", date_range))

# Moderate: 850
for _ in range(850):
    data.append(generate_point(lat_range, lon_range, 1, random.choice(["theft", "minor altercation"]), date_range))

# Unsafe: 800
for _ in range(800):
    data.append(generate_point(lat_range, lon_range, 2, random.choice(["assault", "robbery", "harassment"]), date_range))

# Save
df = pd.DataFrame(data)
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv("visakhapatnam_balanced_crime_data.csv", index=False)
print("✅ Dataset created and saved!")
