from pydantic import BaseModel
from typing import List, Optional
from datetime import date

class Transaction(BaseModel):
    id: str
    category: str
    amount: float
    date: date

class PredictionRequest(BaseModel):
    transactions: List[Transaction]

class CategoryPrediction(BaseModel):
    category: str
    projected_amount: float
    trend: Optional[str] = None

class PredictionResponse(BaseModel):
    predictions: List[CategoryPrediction]

class AnomalyRequest(BaseModel):
    transactions: List[Transaction]

class AnomalyResult(BaseModel):
    transaction_id: str
    is_anomaly: bool
    confidence_score: Optional[float] = None

class AnomalyResponse(BaseModel):
    anomalies: List[AnomalyResult]

class BudgetInsightRequest(BaseModel):
    transactions: List[Transaction]
    monthly_income: float

class BudgetInsightResponse(BaseModel):
    needs_percent: float
    wants_percent: float
    savings_percent: float
    is_balanced: bool
    message: str
    top_category: Optional[str] = None
    recommendation: Optional[str] = None
