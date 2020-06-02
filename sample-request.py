import requests, json

# sample data
data = {'Pclass': 3, 'Age': 2, 'SibSp': 1, 'Fare': 50}

data = json.dumps(data)
url = 'http://127.0.0.1:5000/'
print(data)
send_request = requests.post(url, data)

send_request.json()


#curl localhost:5000/pill -d "{\"task_type\":\"train\", \"source_data\":\"winequality.csv\", \"input_cols\": \"'fixed acidity','volatile acidity','citric acid','residual sugar','chlorides','free sulfur dioxide','total sulfur dioxide','density','pH','sulphates','alcohol'\",  \"target_cols\": \"'quality'\", \"train_freq\":\"daily\"}"  -H 'Content-Type: application/json'
