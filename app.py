from flask import Flask, render_template, jsonify
import random
import datetime
import numpy as np

app = Flask(__name__)

def advanced_prediction():
    real_time_stats = {
        "possession": random.uniform(40, 60),
        "shots_on_goal": random.uniform(0, 10),
        "pass_accuracy": random.uniform(70, 100)
    }

    score = (real_time_stats["possession"] * 0.4 +
             real_time_stats["shots_on_goal"] * 0.3 +
             real_time_stats["pass_accuracy"] * 0.3)
    
    if score > 75:
        trend = 'Bullish'
    elif score < 65:
        trend = 'Bearish'
    else:
        trend = 'Stable'
    
    prediction_result = {
        "trend": trend,
        "confidence": round(score, 2),
        "stats": {k: round(v, 2) for k, v in real_time_stats.items()},
        "time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": "Advanced prediction based on simulated real-time game data."
    }
    
    return prediction_result

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/prediction')
def prediction_page():
    return render_template('prediction.html')

@app.route('/api/prediction')
def api_prediction():
    result = advanced_prediction()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
