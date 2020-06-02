import pandas as pd
from flask import Flask, jsonify, request
import pickle
import sklearn.linear_model._logistic

# app
app = Flask(__name__)

# load model
model = pickle.load(open('model.pkl','rb'))

# routes
@app.route('/', methods=['GET', 'POST'])

def home():
    return "Welcome to ML App"

# routes
@app.route('/predict', methods=['GET','POST'])

def predict():

    # get data
    data = request.get_json(force=True)
    
    # convert data into dataframe
    data.update((x, [y]) for x, y in data.items())
    data_df = pd.DataFrame.from_dict(data)

    # predictions
    result = model.predict(data_df)

    # send back to browser
    output = {'results': int(result[0])}

    # return data
    return jsonify(results=output)

if __name__ == '__main__':
    print("hahahaha")
    app.run(port = 5000, debug=True)