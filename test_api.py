import requests

data = {"text": "This is a subtle API!"}
response = requests.post("http://localhost:5000/predict", json=data)

print(response.json())
