from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# API erstellen
app = FastAPI(title="Housing Price Prediction API")

# Modell laden (Pipeline: Preprocessing + RandomForest)
model = joblib.load("housing_pipeline.pkl")

# Input-Schema für Rohdaten
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
    ocean_proximity: str  # nur KATEGORIE, kein One-Hot Encoding

@app.post("/predict")
def predict(data: HouseData):
    # JSON -> DataFrame
    df = pd.DataFrame([data.dict()])

    # Pipeline kümmert sich um Preprocessing + Vorhersage
    prediction = model.predict(df)[0]

    return {"predicted_price": float(prediction)}
