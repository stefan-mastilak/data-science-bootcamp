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
# 1) Getting data ready
# 2) Choose the right estimator/algorythm for our problems
# 3) Fit the model/algoryth and use it to make predictions on our data
# 4) Evaulating model
# 5) Improve model
# 6) Save and load a trained model
# 7) Putting it all together

# #### Standard imports

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# %matplotlib inline

# ## 1) Get the data ready
#
# Three main things we have to do:
# * Split the data into features and labels (X and Y)
# * Filling (imputing) or disregarding missing values 
# * Converting non-numerical values to numerical values (Feature encoding)

# 1) Load the data from CSV file:
heart_disease = pd.read_csv('data/heart-disease.csv')
heart_disease.head()

# create x (features matrix)
x = heart_disease.drop('target', axis=1)

# create y (labels matrix)
y = heart_disease['target']

# #### 1.0) Split the data into training and test sets:

# data split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# check the split dataset shapes:
x_train.shape, x_test.shape, y_train.shape, y_test.shape

# #### 1.1) Make sure it's all numerical data

# Load car sales data
car_sales = pd.read_csv('data/car-sales-extended.csv')
car_sales.head()

# +
# Split into x and y:
x = car_sales.drop('Price', axis=1)
y = car_sales['Price']

# IMPORTANT: Model cannot deal with strings - we need to transform categories to the numbers
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

categorical_features = ['Make', 'Colour', 'Doors']
one_hot = OneHotEncoder()
transformer = ColumnTransformer([('one_hot', 
                                  one_hot, 
                                  categorical_features)],
                               remainder='passthrough')
transformed_x = transformer.fit_transform(x)
pd.DataFrame(transformed_x).head()
# -

# Build a model:
np.random.seed(42)
x_train, x_test, y_train, y_test = train_test_split(transformed_x, y, test_size=0.2)
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor()
model.fit(x_train, y_train)
model.score(x_test, y_test)


