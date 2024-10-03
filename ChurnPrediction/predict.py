#!/usr/bin/env python
# coding: utf-8

import pickle

from flask import Flask
from flask import request
from flask import jsonify

# parameters

MODEL_FILE = "./model_C=1.0.bin"

# Load the model
with open(MODEL_FILE, "rb") as f_in:
    (dv, model) = pickle.load(f_in)

app = Flask('churn')
@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    churn = y_pred >= 0.5 # This block could be separated into a function

    result = {
        'churn_probability': float(y_pred),
        'churn': bool(churn)
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
