# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# # Scikit-learn introduction
#
# This notebook demonstrates some of the most useful functions of the Sklearn library
#
# What we're going to cover:
#
# 0) End-to-end Scikit-learn workflow
# 1) Getting data ready
# 2) Choose the right estimator/algorythm for our problems
# 3) Fit the model/algoryth and use it to make predictions on our data
# 4) Evaulating model
# 5) Improve model
# 6) Save and load a trained model
# 7) Putting it all together

# ### 1) Get the data ready

# 1) Get the data:
import numpy as np
import pandas as pd
heart_disease = pd.read_csv('data/heart-disease.csv')
heart_disease

# +
# create x (features matrix)
x = heart_disease.drop('target', axis=1)

# create y (labels)
y = heart_disease['target']
# -

# ### 2) Choose the right model and hyperparameters

# +
# import classification machine learning model from sklearn

from sklearn.ensemble import RandomForestClassifier
clf = RandomForestClassifier(n_estimators=100)

# We'll keep the default hyperparameters
clf.get_params()
# -

# ### 3) Fit the model to the training data

# +
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
# -

clf.fit(x_train, y_train);

y_preds = clf.predict(x_test)
y_preds

# ### 4) Evaulate the model on training data and test data

# check model score on training data
clf.score(x_train, y_train)

# check model score on test data
clf.score(x_test, y_test)

# +
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

print(classification_report(y_test, y_preds))
# -

confusion_matrix(y_test, y_preds)

accuracy_score(y_test, y_preds)

# ### 5) Improve a model
#
# Try different amount of n_estimators

# +
np.random.seed(42)

for i in range(10,100,10):
    print(f'Tryting model with {i} estimators..')
    clf = RandomForestClassifier(n_estimators=i).fit(x_train, y_train)
    print(f'Model accuracy on test set: {(clf.score(x_test, y_test) * 100).round(2)}%')
    print("")

# -

# ### 6) Save a model and load it

# +
import pickle

pickle.dump(clf, open('models/random_forest_model_1.pkl', 'wb'))
# -

loaded = pickle.load(open('models/random_forest_model_1.pkl', 'rb'))
loaded.score(x_test, y_test)


