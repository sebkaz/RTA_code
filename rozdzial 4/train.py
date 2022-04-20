import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from joblib import dump
from model import Perceptron
# dane 
iris = load_iris()
df = pd.DataFrame(data=np.c_[iris['data'], iris['target']],
                  columns=iris['feature_names']+ ['target'])
X = df.iloc[:100, [0,2]].values
y = df.iloc[:100, 4].values
y = np.where(y==0,-1,1)
# model train
clf = Perceptron()
clf.fit(X, y)
dump(clf, './model.joblib')