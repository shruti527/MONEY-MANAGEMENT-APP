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
            is_balanced=False, message="Monthly income must be greater than 0.",
            recommendation="Please enter a valid monthly income."
        )

    needs_categories = ['Housing', 'Groceries', 'Utilities', 'Transportation', 'Healthcare']
    wants_categories = ['Dining', 'Entertainment', 'Shopping', 'Travel']

    total_needs = sum(t.amount for t in transactions if t.category in needs_categories)
    total_wants = sum(t.amount for t in transactions if t.category in wants_categories)
    total_spent = sum(t.amount for t in transactions)
    total_savings = income - total_spent

    needs_pct = (total_needs / income) * 100 if income > 0 else 0
    wants_pct = (total_wants / income) * 100 if income > 0 else 0
    savings_pct = (total_savings / income) * 100 if income > 0 else 0

    category_totals = {}
    for t in transactions:
        category_totals[t.category] = category_totals.get(t.category, 0) + t.amount

    top_category = None
    if category_totals:
        top_category = max(category_totals, key=category_totals.get)
        top_amount = category_totals[top_category]
    else:
        top_amount = 0

    is_balanced = needs_pct <= 55 and wants_pct <= 35 and savings_pct >= 15

    if not transactions:
        msg = "Add transactions to see clear budget insights."
        recommendation = "Start by logging your recent expenses and income."
    elif is_balanced:
        msg = (
            f"Strong work! Your budget is balanced: {needs_pct:.0f}% needs, "
            f"{wants_pct:.0f}% wants, and {savings_pct:.0f}% savings."
        )
        recommendation = "Keep tracking your spending and maintain this healthy mix."
    elif needs_pct > 50:
        msg = (
            f"Your fixed needs are using {needs_pct:.0f}% of your income. "
            "This can make it harder to save."
        )
        recommendation = "Review bills, subscriptions, and utility costs to reduce essential spending."
    elif wants_pct > 30:
        msg = (
            f"Discretionary spending is at {wants_pct:.0f}% of income. "
            "That leaves less for savings."
        )
        recommendation = "Cut back on non-essentials like dining out or entertainment."
    else:
        msg = (
            f"Your savings rate is {savings_pct:.0f}%. "
            "Try increasing it toward 20% for a stronger budget."
        )
        recommendation = "Set a small monthly savings target and keep your spending steady."

    if top_category and top_amount > 0:
        msg += f" Your largest spending category is {top_category} (₹{top_amount:.0f})."

    return BudgetInsightResponse(
        needs_percent=round(needs_pct, 2),
        wants_percent=round(wants_pct, 2),
        savings_percent=round(savings_pct, 2),
        is_balanced=is_balanced,
        message=msg,
        top_category=top_category,
        recommendation=recommendation
    )
