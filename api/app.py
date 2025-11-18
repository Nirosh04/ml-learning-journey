from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, validator
import joblib
import os
import pandas as pd
import time
import logging

# ---------------------------------------------------
# Logger konfigurieren
# ---------------------------------------------------
logger = logging.getLogger("housing-api")
logger.setLevel(logging.INFO)

handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)
handler.setFormatter(formatter)

# Verhindert doppelte Handler, falls Uvicorn auch konfiguriert
if not logger.handlers:
    logger.addHandler(handler)

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
model_path = os.path.join(os.path.dirname(__file__), "housing_pipeline.pkl")

try:
    model = joblib.load(model_path)
    logger.info(f"Modell erfolgreich geladen von: {model_path}")
except Exception as e:
    logger.exception(f"Fehler beim Laden des Modells unter {model_path}: {e}")
    # harter Fehler: ohne Modell macht die API keinen Sinn
    raise RuntimeError("Model konnte nicht geladen werden")

# ---------------------------------------------------
# Pydantic Input Schema
# ---------------------------------------------------
VALID_OCEAN_VALUES = {
    "NEAR BAY",
    "INLAND",
    "NEAR OCEAN",
    "ISLAND",
    "1H OCEAN",
}


class HouseData(BaseModel):
    longitude: float = Field(..., ge=-180, le=180)
    latitude: float = Field(..., ge=-90, le=90)
    housing_median_age: float = Field(..., ge=0)
    total_rooms: float = Field(..., ge=0)
    total_bedrooms: float = Field(..., ge=0)
    population: float = Field(..., ge=0)
    households: float = Field(..., ge=0)
    median_income: float = Field(..., ge=0)
    rooms_per_household: float = Field(..., ge=0)
    bedrooms_per_room: float = Field(..., ge=0)
    population_per_household: float = Field(..., ge=0)
    ocean_proximity: str

    @validator("ocean_proximity")
    def validate_ocean_proximity(cls, v: str) -> str:
        v_upper = v.upper()
        if v_upper not in VALID_OCEAN_VALUES:
            raise ValueError(
                f"ocean_proximity muss einer dieser Werte sein: {VALID_OCEAN_VALUES}"
            )
        return v_upper


# ---------------------------------------------------
# Globaler Error-Handler (Production Pattern)
# ---------------------------------------------------
@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled error: {exc}")
    return JSONResponse(
        status_code=500,
        content={"detail": "Internal server error"},
    )


# ---------------------------------------------------
# Prediction Endpoint
# ---------------------------------------------------
@app.post("/predict")
def predict(data: HouseData):
    global total_requests, total_latency

    start = time.time()
    total_requests += 1

    logger.info(f"Request #{total_requests}: Input = {data.model_dump()}")

    # Pydantic-Objekt -> DataFrame
    df = pd.DataFrame([data.model_dump()])

    try:
        prediction = float(model.predict(df)[0])
    except Exception as e:
        logger.error(f"Prediction Error: {str(e)}")
        raise HTTPException(status_code=400, detail=f"Model Error: {str(e)}")

    latency = time.time() - start
    total_latency += latency

    logger.info(f"Antwortzeit = {latency:.4f} Sekunden, Prediction = {prediction}")

    return {
        "predicted_price": prediction,
        "latency_sec": latency,
    }


# ---------------------------------------------------
# Monitoring Endpoint
# ---------------------------------------------------
@app.get("/metrics")
def metrics():
    avg_latency = total_latency / total_requests if total_requests > 0 else 0.0

    return {
        "total_requests": total_requests,
        "average_latency_sec": avg_latency,
    }


# ---------------------------------------------------
# Healthcheck Endpoint (für Render)
# ---------------------------------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ---------------------------------------------------
# Root Endpoint
# ---------------------------------------------------
@app.get("/")
def root():
    return {
        "message": "Housing Prediction API läuft",
        "endpoints": {
            "/": "Root",
            "/health": "Healthcheck",
            "/predict": "Vorhersagen",
            "/metrics": "Monitoring",
        },
    }







