import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import date
from typing import List
from app.schemas import Transaction, CategoryPrediction

def predict_spending(transactions: List[Transaction]) -> List[CategoryPrediction]:
    if not transactions:
        return []

    # Convert to DataFrame
    df = pd.DataFrame([t.model_dump() for t in transactions])
    
    # Extract year and month for aggregation
    df['date'] = pd.to_datetime(df['date'])
    df['year_month'] = df['date'].dt.to_period('M')
    
    # Aggregate by month and category
    monthly_cat = df.groupby(['year_month', 'category'])['amount'].sum().reset_index()
    
    predictions = []
    categories = df['category'].unique()
    
    for cat in categories:
        cat_data = monthly_cat[monthly_cat['category'] == cat].copy()
        
        # Sort chronologically
        cat_data = cat_data.sort_values('year_month')
        
        if len(cat_data) < 1:
            continue
        elif len(cat_data) < 3:
            # Fallback: Moving Average (or just average if very few points)
            projected = cat_data['amount'].mean()
        else:
            # Linear Regression
            # Create a simple time index
            cat_data['time_index'] = np.arange(len(cat_data))
            
            X = cat_data[['time_index']]
            y = cat_data['amount']
            
            model = LinearRegression()
            model.fit(X, y)
            
            # Predict next month (time_index = len(cat_data))
            next_index = np.array([[len(cat_data)]])
            projected = model.predict(next_index)[0]
            
            # Ensure we don't predict negative spending
            projected = max(0, projected)
            
        predictions.append(CategoryPrediction(category=cat, projected_amount=round(projected, 2)))
        
    return predictions
