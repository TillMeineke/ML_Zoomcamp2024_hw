#!/usr/bin/env python
# coding: utf-8

import pickle

from flask import Flask, jsonify, request

from typing import Dict, Any, List

# parameters

# MODEL_FILE = "./models/model_md=20_msl=5.bin" # local testing without docker
MODEL_FILE = "./model_md=20_msl=5.bin"  # testing with docker

# load model
with open(MODEL_FILE, "rb") as f_in:
    (dv, model) = pickle.load(f_in)

app = Flask("fungi-classifier")


@app.route("/predict", methods=["POST"])
def predict():
    """
    Predict the type of fungi based on input data.

    This function receives input data in JSON format via a request,
    transforms it using a pre-fitted DictVectorizer, and then uses
    a pre-trained model to predict the type of fungi.

        Response: A JSON response containing the predicted type of fungi.
    """
    fungi: Dict[str, Any] = request.get_json()

    X = dv.transform([fungi])
    prediction: List[Any] = model.predict(X)

    # print(f"Predicted fungi: {prediction[0]}")

    return jsonify({"fungi": prediction[0]})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=9696)
