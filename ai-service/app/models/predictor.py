import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from datetime import date
from typing import List
from app.schemas import Transaction, CategoryPrediction

def predict_spending(transactions: List[Transaction]) -> List[CategoryPrediction]:
    if not transactions:
        return []

    df = pd.DataFrame([t.model_dump() for t in transactions])
    df['date'] = pd.to_datetime(df['date'])
    df['year_month'] = df['date'].dt.to_period('M')

    monthly_cat = df.groupby(['year_month', 'category'])['amount'].sum().reset_index()
    predictions = []
    categories = df['category'].unique()

    for cat in categories:
        cat_data = monthly_cat[monthly_cat['category'] == cat].copy()
        cat_data = cat_data.sort_values('year_month')

        if len(cat_data) == 0:
            continue

        if len(cat_data) < 2:
            projected = cat_data['amount'].mean()
            trend = 'Needs more data'
        elif len(cat_data) == 2:
            projected = cat_data['amount'].mean()
            last_change = cat_data['amount'].iloc[-1] - cat_data['amount'].iloc[-2]
            if abs(last_change) < cat_data['amount'].mean() * 0.1:
                trend = 'Stable'
            elif last_change > 0:
                trend = 'Increasing'
            else:
                trend = 'Decreasing'
        else:
            cat_data['time_index'] = np.arange(len(cat_data))
            X = cat_data[['time_index']]
            y = cat_data['amount']

            model = LinearRegression()
            model.fit(X, y)

            next_index = np.array([[len(cat_data)]])
            projected = model.predict(next_index)[0]
            projected = max(0, projected)

            slope = float(model.coef_[0])
            avg_amount = cat_data['amount'].mean() if cat_data['amount'].mean() != 0 else 1
            if slope > avg_amount * 0.05:
                trend = 'Increasing'
            elif slope < -avg_amount * 0.05:
                trend = 'Decreasing'
            else:
                trend = 'Stable'

        predictions.append(
            CategoryPrediction(
                category=cat,
                projected_amount=round(projected, 2),
                trend=trend,
            )
        )

    predictions = sorted(predictions, key=lambda p: p.projected_amount, reverse=True)
    return predictions
