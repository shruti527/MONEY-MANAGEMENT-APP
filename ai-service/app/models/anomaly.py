import pandas as pd
from sklearn.ensemble import IsolationForest
from typing import List
from app.schemas import Transaction, AnomalyResult

def detect_anomalies(transactions: List[Transaction]) -> List[AnomalyResult]:
    if not transactions:
        return []
        
    if len(transactions) < 5:
        # Not enough data for meaningful anomaly detection
        return [AnomalyResult(transaction_id=t.id, is_anomaly=False) for t in transactions]

    # Convert to DataFrame
    df = pd.DataFrame([t.model_dump() for t in transactions])
    
    # We'll use the 'amount' feature for anomaly detection
    # In a real scenario, we might encode category or use date features too
    X = df[['amount']]
    
    # Initialize IsolationForest
    # contamination=0.1 means we expect roughly 10% of data to be outliers
    model = IsolationForest(contamination=0.1, random_state=42)
    
    # Fit and predict (-1 for anomalies, 1 for normal)
    predictions = model.fit_predict(X)
    
    # Get anomaly scores (lower means more abnormal)
    scores = model.decision_function(X)
    
    results = []
    for idx, row in df.iterrows():
        is_anomaly = bool(predictions[idx] == -1)
        # Normalize score slightly for easier interpretation, though raw score is fine
        confidence = float(abs(scores[idx])) 
        
        results.append(AnomalyResult(
            transaction_id=str(row['id']),
            is_anomaly=is_anomaly,
            confidence_score=confidence
        ))
        
    return results
