from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import pandas as pd

# Initialize the FastAPI app
app = FastAPI()

# Load the trained model
model = joblib.load("../models/sales_model.pkl")

# Define the input data structure
class SalesPredictionRequest(BaseModel):
    Store: int
    DayOfWeek: int
    Promo: int
    StateHoliday: str
    SchoolHoliday: int
    CompetitionDistance: float
    Year: int
    Month: int
    Weekday: int


@app.get("/predict")
def predict_sales(input_data: SalesPredictionRequest):
    try:
        data = pd.DataFrame([input_data.dict()])        
        prediction = model.predict(data)        
        return {"predicted_sales": prediction[0]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {str(e)}")

@app.get("/")
def read_root():
    return {"Hello": "World"}