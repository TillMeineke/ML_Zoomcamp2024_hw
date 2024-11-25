#!/usr/bin/env python
# coding: utf-8


import requests
import pandas as pd

host = "fungi-classifier.eba-rpcwcrqg.eu-central-1.elasticbeanstalk.com"  # AWS Elastic Beanstalk (remote)
# host = "18.199.224.106:9696"
# host = "mlzoomcamp-tm.spdns.de:9696"
# host = "127.0.0.1:9696"  # local
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
    "cap-diameter": 7.0,
    "stem-height": 8.0,
    "stem-width": 1.0,
}


response = requests.post(url, json=random_fungi).json()
#response.value()

primary_data = pd.read_csv("./data/raw/primary_data_edited.csv", sep=";")

pred_overview = primary_data[primary_data["name"] == response["fungi"]]
#pred_overview
#overview = primary_data[primary_data["name"] == "Soft Slipper Toadstool"]



print(pred_overview.T)
