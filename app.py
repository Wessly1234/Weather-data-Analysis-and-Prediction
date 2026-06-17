from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load dataset
df = pd.read_csv("weather.csv")

# Convert date
df['Date'] = pd.to_datetime(df['Date'])

# Create day number
df['Day_Number'] = np.arange(len(df))

# Train Model
X = df[['Day_Number']]
y = df['Temperature']

model = LinearRegression()
model.fit(X, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analysis')
def analysis():

    data = {
        "max_temp": round(df['Temperature'].max(), 2),
        "min_temp": round(df['Temperature'].min(), 2),
        "avg_temp": round(df['Temperature'].mean(), 2),
        "total_days": len(df)
    }

    return jsonify(data)

@app.route('/chart')
def chart():

    chart_data = {
        "dates": df['Date'].dt.strftime('%Y-%m-%d').tolist(),
        "temps": df['Temperature'].tolist()
    }

    return jsonify(chart_data)

@app.route('/predict', methods=['POST'])
def predict():

    future_day = int(request.form['day'])

    prediction = model.predict([[future_day]])

    return jsonify({
        "predicted_temperature": round(float(prediction[0]), 2)
    })

if __name__ == "__main__":
    app.run(debug=True)
