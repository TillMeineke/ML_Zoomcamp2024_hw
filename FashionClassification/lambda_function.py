#!/usr/bin/env python
# coding: utf-8

# import tensorflow.lite as tflite

import json
import tflite_runtime.interpreter as tflite
from keras_image_helper import create_preprocessor

# Create a preprocessor for the model
preprocessor = create_preprocessor("xception", target_size=(299, 299))

# Load the TFLite model and get indices of input and output tensors
interpreter = tflite.Interpreter("./models/clothing_model.tflite")
interpreter.allocate_tensors()

input_index = interpreter.get_input_details()[0]["index"]
output_index = interpreter.get_output_details()[0]["index"]


# Post-processing: get the class name of the highest probability
classes = [
    "dress",
    "hat",
    "longsleeve",
    "outwear",
    "pants",
    "shirt",
    "shoes",
    "shorts",
    "skirt",
    "t-shirt",
]

# url = "http://bit.ly/mlbookcamp-pants"


def predict(url):
    """Load an image from a URL and preprocess it"""
    X = preprocessor.from_url(url)

    # Run the model
    interpreter.set_tensor(input_index, X)
    interpreter.invoke()
    preds = interpreter.get_tensor(output_index)

    float_predictions = preds[0].tolist()

    return dict(zip(classes, float_predictions))


def lambda_handler(event, context):
    #print("parameters:", event)
    url = event["url"]
    result = predict(url)
    return result
