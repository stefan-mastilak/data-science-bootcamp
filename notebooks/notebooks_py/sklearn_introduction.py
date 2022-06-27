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

# ## 0. End to end Scikit-Learn workflow

# 1) Get the data ready:
import pandas as pd
heart_disease = pd.read_csv('data/heart-disease.csv')
heart_disease


# +
# create x (features matrix)
x = heart_disease.drop('target', axis=1)

# create y (labels)
y = heart_disease['target']
# -

# 2) Choose the right model and hyperparameters
from sklearn.ensemble import RandomForestClassifier


