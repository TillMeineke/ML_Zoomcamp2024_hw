#!/usr/bin/env python
# coding: utf-8


import requests
import pandas as pd

# host = "churn-serving-env.eba-vzejz2a6.eu-central-1.elasticbeanstalk.com"  # AWS Elastic Beanstalk (remote)
host = "127.0.0.1:9696"  # local
# host = "localhost:9696" # local
url = f"http://{host}/predict"

random_fungi = {
    "cap-shape": "x",
    "cap-color": "o",
    "does-bruise-or-bleed": "f",
    "gill-color": "w",
    "stem-color": "w",
    "has-ring": "t",
    "habitat": "d",
    "season": "w",
    "cap-diameter": 15.0,
    "stem-height": 1.0,
    "stem-width": 15.0,
}


response = requests.post(url, json=random_fungi).json()
#response.value()

primary_data = pd.read_csv("./data/raw/primary_data_edited.csv", sep=";")

pred_overview = primary_data[primary_data["name"] == response["fungi"]]
#pred_overview
#overview = primary_data[primary_data["name"] == "Soft Slipper Toadstool"]



print(pred_overview.T)

# if response["churn"] == True:
#     print("sending promo email to %s" % customer_id)
# else:
#     print("not sending promo email to %s" % customer_id)
