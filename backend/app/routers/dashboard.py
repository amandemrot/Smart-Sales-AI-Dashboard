from fastapi import APIRouter
from app.services.data_processor import DataProcessor
from pydantic import BaseModel
from typing import List

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])
data_processor = DataProcessor()

# ---------------- MODELS ----------------

class Metric(BaseModel):
    value: float
    changeDescription: str

class KeyMetrics(BaseModel):
    totalRevenue: Metric
    activeUsers: Metric
    salesGrowth: Metric

class SalesHistory(BaseModel):
    month: str
    sales: float

class SalesForecast(BaseModel):
    date: str
    product: str
    forecast: float
    lowerBound: float
    upperBound: float

# ---------------- ENDPOINTS ----------------

@router.get("/key-metrics", response_model=KeyMetrics)
def get_key_metrics():
    return data_processor.calculate_key_metrics()

@router.get("/sales-history", response_model=List[SalesHistory])
def get_sales_history():
    # Dummy history so graph always loads
    return [
        {"month":"Jan","sales":32000},
        {"month":"Feb","sales":41000},
        {"month":"Mar","sales":39000},
        {"month":"Apr","sales":52000},
        {"month":"May","sales":61000},
        {"month":"Jun","sales":70000}
    ]

@router.get("/sales-forecast", response_model=List[SalesForecast])
def get_sales_forecast():
    return data_processor.calculate_sales_forecast()

@router.get("")
def dashboard_root():
    return {"message": "Dashboard API root"}
