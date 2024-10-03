import requests

# url = "http://localhost:8080/2015-03-31/functions/function/invocations" #from
# url = 'http://localhost:9696/predict' # for 10.3 Pre-Processing Service
url = 'http://localhost:8080/predict'
data = {"url": "http://bit.ly/mlbookcamp-pants"}

result = requests.post(url, json=data).json()
print(result)