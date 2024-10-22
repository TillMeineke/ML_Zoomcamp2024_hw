import requests

url = "http://localhost:9696/predict" # local
# url = "http://ec2-18-159-215-56.eu-central-1.compute.amazonaws.com:9696/predict" # aws

client = {"job": "management", "duration": 400, "poutcome": "success"}
response = requests.post(url, json=client).json()

print(response)
