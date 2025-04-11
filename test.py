# Generate random requests to the Flask API and print the responses

import requests
import random
from datetime import datetime, timedelta

# make sure that the Flask API is running locally
API_URL = "http://127.0.0.1:5000/predict"  

LAT_RANGE = (17.70, 17.75)
LON_RANGE = (83.28, 83.35)

def generate_random_request():
    lat = round(random.uniform(*LAT_RANGE), 6)
    lon = round(random.uniform(*LON_RANGE), 6)
    random_time = datetime.now() - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))
    date_time = random_time.strftime("%Y-%m-%d %H:%M:%S")

    return {
        "latitude": lat,
        "longitude": lon,
        "date_time": date_time
    }

for i in range(10):
    payload = generate_random_request()
    response = requests.post(API_URL, json=payload)
    print(f"Request #{i+1} | Input: {payload}")
    print("Response:", response.json(), "\n")
