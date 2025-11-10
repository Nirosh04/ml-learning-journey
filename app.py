from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd
import time
import logging

# ---------------------------------------------------
# Logging konfigurieren
# ---------------------------------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

# ---------------------------------------------------
# FastAPI App
# ---------------------------------------------------
app = FastAPI(title="Housing Price Prediction API")

# ---------------------------------------------------
# Monitoring Variablen
# ---------------------------------------------------
total_requests = 0
total_latency = 0.0

# ---------------------------------------------------
# Modell laden (Pipeline)
# ---------------------------------------------------
model = joblib.load("housing_pipeline.pkl")

# ---------------------------------------------------
# Input Schema
# ---------------------------------------------------
class HouseData(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    rooms_per_household: float
    bedrooms_per_room: float
    population_per_household: float
    ocean_proximity: str

# ---------------------------------------------------
# Prediction Endpoint
# ---------------------------------------------------
@app.post("/predict")
def predict(data: HouseData):
    global total_requests, total_latency

    start = time.time()
    total_requests += 1

    logging.info(f"Request #{total_requests}: Input = {data.dict()}")

    df = pd.DataFrame([data.dict()])

    try:
        prediction = float(model.predict(df)[0])
    except Exception as e:
        logging.error(f"Prediction Error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Model Error: {str(e)}")

    latency = time.time() - start
    total_latency += latency

    logging.info(f"Antwortzeit = {latency:.4f} Sekunden")

    return {
        "predicted_price": prediction,
        "latency_sec": latency
    }

# ---------------------------------------------------
# Monitoring Endpoint
# ---------------------------------------------------
@app.get("/metrics")
def metrics():
    avg_latency = total_latency / total_requests if total_requests > 0 else 0

    return {
        "total_requests": total_requests,
        "average_latency_sec": avg_latency
    }

# ---------------------------------------------------
# Root Endpoint
# ---------------------------------------------------
@app.get("/")
def root():
    return {
        "message": "Housing Prediction API läuft",
        "endpoints": {
            "/predict": "Vorhersagen",
            "/metrics": "Monitoring"
        }
    }










