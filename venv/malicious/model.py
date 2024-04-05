
"""
Created on Thu Apr 22 19:47:00 2021

@author: Sankalp
"""


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score
from sklearn.neural_network import MLPClassifier


data0 = pd.read_csv('/DataFiles/5.urldata.csv')
data = data0.drop(['Domain'], axis = 1).copy()


data = data.sample(frac=1).reset_index(drop=True)
y = data['Label']
X = data.drop('Label',axis=1)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 12)

ML_Model = []
acc_train = []
acc_test = []


def storeResults(model, a,b):
  ML_Model.append(model)
  acc_train.append(round(a, 3))
  acc_test.append(round(b, 3))
  
  



mlp = MLPClassifier(alpha=0.001, hidden_layer_sizes=([100,100,100]))

mlp.fit(X_train, y_train)


y_test_mlp = mlp.predict(X_test)
y_train_mlp = mlp.predict(X_train)



import joblib
joblib.dump(mlp, 'mlp.pkl')


