import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

# Load dataset
df = pd.read_csv("visakhapatnam_balanced_crime_data.csv")

# Convert datetime
df["date_time"] = pd.to_datetime(df["date_time"])
df["hour"] = df["date_time"].dt.hour
df["dayofweek"] = df["date_time"].dt.dayofweek

# Features and target
X = df[["latitude", "longitude", "hour", "dayofweek"]]
y = df["safety_level"]  # ← Updated here

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(n_estimators=150, random_state=42))
])

# Train and save
pipeline.fit(X_train, y_train)
joblib.dump(pipeline, "hersafe_model_v2.pkl")
print("✅ Model trained and saved as 'hersafe_model_v2.pkl'")
