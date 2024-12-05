import requests

# url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
url = "https://wvlp6tz2g2.execute-api.eu-central-1.amazonaws.com/test/predict"

data = {
    "url": "https://habrastorage.org/webt/yf/_d/ok/yf_dokzqy3vcritme8ggnzqlvwa.jpeg"
}

result = requests.post(url, json=data).json()
print(result)
