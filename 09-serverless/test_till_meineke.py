import requests

url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
# url = "https://727646501899.dkr.ecr.eu-central-1.amazonaws.com/clothing-tflite-images"
# url = "https://727646501899.dkr.ecr.eu-central-1.amazonaws.com/clothing-tflite-images:clothing-model-xception-v4-001"

data = {
    "url": "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"
}

result = requests.post(url, json=data).json()
print(result)
