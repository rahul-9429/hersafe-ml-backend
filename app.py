import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd
from datetime import datetime

model = joblib.load('hersafe_model_v2.pkl')

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return "HerSafe ML API is running."

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        latitude = float(data["latitude"])
        longitude = float(data["longitude"])
        date_time_str = data["date_time"]
        date_time = datetime.strptime(date_time_str, "%Y-%m-%d %H:%M:%S")

        hour = date_time.hour
        dayofweek = date_time.weekday()

        df = pd.DataFrame([{
            "latitude": latitude,
            "longitude": longitude,
            "hour": hour,
            "dayofweek": dayofweek
        }])

        prediction = model.predict(df)[0]
        result = "unsafe" if prediction == 1 else "safe"

        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    print("✅ Flask app is starting...")
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 5000)))
