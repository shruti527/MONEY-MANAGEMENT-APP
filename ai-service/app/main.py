from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import (
    PredictionRequest, PredictionResponse,
    AnomalyRequest, AnomalyResponse,
    BudgetInsightRequest, BudgetInsightResponse
)
from app.models.predictor import predict_spending
from app.models.anomaly import detect_anomalies

app = FastAPI(title="Money Management AI Service")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify the exact Next.js origin
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.post("/api/v1/predict-spending", response_model=PredictionResponse)
def api_predict_spending(request: PredictionRequest):
    predictions = predict_spending(request.transactions)
    return PredictionResponse(predictions=predictions)

@app.post("/api/v1/detect-anomalies", response_model=AnomalyResponse)
def api_detect_anomalies(request: AnomalyRequest):
    anomalies = detect_anomalies(request.transactions)
    return AnomalyResponse(anomalies=anomalies)

@app.post("/api/v1/budget-insights", response_model=BudgetInsightResponse)
def api_budget_insights(request: BudgetInsightRequest):
    transactions = request.transactions
    income = request.monthly_income
    
    if income <= 0:
        return BudgetInsightResponse(
            needs_percent=0, wants_percent=0, savings_percent=0,
            is_balanced=False, message="Monthly income must be greater than 0."
        )

    # Simplified categorization logic for demonstration
    # In reality, you'd map specific user categories to Needs/Wants
    needs_categories = ['Housing', 'Groceries', 'Utilities', 'Transportation', 'Healthcare']
    wants_categories = ['Dining', 'Entertainment', 'Shopping', 'Travel']
    
    total_needs = sum(t.amount for t in transactions if t.category in needs_categories)
    total_wants = sum(t.amount for t in transactions if t.category in wants_categories)
    
    # Savings can be inferred by what's left, or specific categories
    total_spent = sum(t.amount for t in transactions)
    total_savings = income - total_spent
    
    needs_pct = (total_needs / income) * 100
    wants_pct = (total_wants / income) * 100
    savings_pct = (total_savings / income) * 100
    
    # 50/30/20 Rule: 50% Needs, 30% Wants, 20% Savings
    is_balanced = needs_pct <= 55 and wants_pct <= 35 and savings_pct >= 15
    
    if is_balanced:
        msg = "Great job! Your spending aligns well with the 50/30/20 budget rule."
    elif needs_pct > 50:
        msg = f"Your needs are taking up {needs_pct:.1f}% of your income. Consider finding ways to lower fixed costs."
    elif wants_pct > 30:
        msg = f"You are spending {wants_pct:.1f}% on wants. Try cutting back on discretionary spending."
    else:
        msg = f"Your savings rate is {savings_pct:.1f}%. Try to aim for 20% by reducing expenses."

    return BudgetInsightResponse(
        needs_percent=round(needs_pct, 2),
        wants_percent=round(wants_pct, 2),
        savings_percent=round(savings_pct, 2),
        is_balanced=is_balanced,
        message=msg
    )
