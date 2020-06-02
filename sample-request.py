import requests, json
"""
# sample data
data = "{\"Pclass\": 3, \"Age\": 2, \"SibSp\": 1, \"Fare\": 50}"

data = json.dumps(data)
url = 'http://127.0.0.1:5000/'
print(data)
send_request = requests.post(url, data)

send_request.json()
"""
curl localhost:5000/predict -d "{\"Pclass\": 3, \"Age\": 2, \"SibSp\": 1, \"Fare\": 50}"  -H 'Content-Type: application/json'
