import pandas as pd
import _pickle as pickle
import os
from sklearn.linear_model import *

## Check current working directory
os.getcwd()

# create df
train = pd.read_csv('titanic.csv') # change file path

# drop null values
train.dropna(inplace=True)

# features and target
target = 'Survived'
features = ['Pclass', 'Age', 'SibSp', 'Fare']

# X matrix, y vector
X = train[features]
y = train[target]

model = LogisticRegression()
model.fit(X, y)
model.score(X, y)

## export model to a pickel file
pickle.dump(model, open('model.pkl', 'wb'))