import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
import joblib

# Load unsafe and safe datasets
unsafe_df = pd.read_csv("visakhapatnam_crime_data.csv")
safe_df = pd.read_csv("safe_data_vizag.csv")

# Ensure correct datetime format
unsafe_df["date_time"] = pd.to_datetime(unsafe_df["date_time"])
safe_df["date_time"] = pd.to_datetime(safe_df["date_time"])

# Add "None" as crime_type for safe data
safe_df["crime_type"] = "None"

# Merge both datasets
df = pd.concat([unsafe_df, safe_df], ignore_index=True)

# Feature engineering
df["hour"] = df["date_time"].dt.hour
df["dayofweek"] = df["date_time"].dt.dayofweek
df["is_unsafe"] = df["crime_type"].apply(lambda x: 0 if str(x).strip().lower() == "none" else 1)

# Select features and label
X = df[["latitude", "longitude", "hour", "dayofweek"]]
y = df["is_unsafe"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("classifier", RandomForestClassifier(n_estimators=150, random_state=42))
])

# Train model
pipeline.fit(X_train, y_train)

# Save the trained model
joblib.dump(pipeline, "hersafe_model_v2.pkl")
print("✅ Model trained and saved as 'hersafe_model_v2.pkl'")
