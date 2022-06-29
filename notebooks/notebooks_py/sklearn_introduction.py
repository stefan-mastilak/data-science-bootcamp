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

# # 1 - Get the data ready
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

# ### 1.0) Split the data into training and test sets:

# data split
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# check the split dataset shapes:
x_train.shape, x_test.shape, y_train.shape, y_test.shape

# ### 1.1) Make sure it's all numerical data

# Load car sales data
car_sales = pd.read_csv('data/car-sales-extended.csv')
car_sales.head()

len(car_sales)

car_sales.dtypes

# #### Convert non-numerical data into numeric

# +
# Split into x and y:
x = car_sales.drop('Price', axis=1)
y = car_sales['Price']

# IMPORTANT: Model cannot deal with strings
# WORKAROUND: Transform categories to the numbers

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

# NOTE: We need to threat doors as a categorical column, because
# multiple cars are in this category (with 4 doors, 5 doors etc.)

categorical_features = ['Make', 'Colour', 'Doors']

# instatiate one hot encoder:
one_hot = OneHotEncoder()

# define transformer:
transformer = ColumnTransformer([('one_hot', 
                                  one_hot, 
                                  categorical_features)],
                               remainder='passthrough')

# transform categorical columns into the numbers:
transformed_x = transformer.fit_transform(x)

# put transformed data into the pandas dataframe:
pd.DataFrame(transformed_x).head()
# -

dummies = pd.get_dummies(car_sales[['Make', 'Colour', 'Doors']])
dummies.head()

# +
# Build a model:
np.random.seed(42)
x_train, x_test, y_train, y_test = train_test_split(transformed_x, y, test_size=0.2)

from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(x_train, y_train)
model.score(x_test, y_test)
# -

# ### 1.2) What if there are missing values?
#
# 1. Fill them with some value (also known as imputation)
# 2. Remove the samples with missing data altogether

# Import car sales missing data:
car_sales_missing = pd.read_csv('data/car-sales-extended-missing-data.csv')
car_sales_missing.head(8)

# Get the sum of the missing columns in the data:
car_sales_missing.isna().sum()

# Drop the rows with no labels (our case - those with no Price label)
# NOTE: those data are irrelevant, because label is missing here
car_sales_missing.dropna(subset=["Price"], inplace=True)
car_sales_missing.isna().sum()

# Note: 50 rows will be missing - so 950 rows remained in dataset:
len(car_sales_missing)

# +
# Split into x and y:
x = car_sales_missing.drop('Price', axis=1)
y = car_sales_missing['Price']

# Split the data into training and test sets:
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# check the split dataset shapes:
x_train.shape, x_test.shape, y_train.shape, y_test.shape
# -

# ### Option1: Fill the missing data with Pandas:

# +
# fill up the make column
car_sales_missing['Make'].fillna('missing', inplace=True)

# fill up the colour column:
car_sales_missing['Colour'].fillna('missing', inplace=True)

# fill up the odometer column:
car_sales_missing['Odometer (KM)'].fillna(car_sales_missing['Odometer (KM)'].mean(), inplace=True)

# fill up the doors column:
car_sales_missing['Doors'].fillna(4, inplace=True)

# check missing data again:
car_sales_missing.isna().sum()

# +
# Let's try to convert that into the numbers:

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

categorical_features = ['Make', 'Colour', 'Doors']
one_hot = OneHotEncoder()
transformer = ColumnTransformer([('one_hot', 
                                  one_hot, 
                                  categorical_features)],
                                  remainder='passthrough')

transformed_x = transformer.fit_transform(car_sales_missing)
transformed_x
# -

# ### Option2: Fill the mising values with scikit-learn
# The main takeaways:
#
# 1. Split your data first (into train/test)
# 2. Fill/transform the training set and test sets separately
#
# NOTE:   It's best to fill and transform training and test sets separately

# load data:
car_sales_missing = pd.read_csv("data/car-sales-extended-missing-data.csv")
car_sales_missing.head()

# check missing data:
car_sales_missing.isna().sum()

# Drop the rows with no labels
car_sales_missing.dropna(subset=["Price"], inplace=True)
car_sales_missing.isna().sum()

# +
# Split into X & y
x = car_sales_missing.drop("Price", axis=1)
y = car_sales_missing["Price"]

# Split data into train and test
np.random.seed(42)
x_train, x_test, y_train, y_test = train_test_split(x,
                                                    y,
                                                    test_size=0.2)
# -

# Check missing values
x.isna().sum()

# +
# Fill missing values with Scikit-Learn
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

# Fill categorical values with 'missing' & numerical values with mean
cat_imputer = SimpleImputer(strategy="constant", fill_value="missing")
door_imputer = SimpleImputer(strategy="constant", fill_value=4)
num_imputer = SimpleImputer(strategy="mean")

# Define columns
cat_features = ["Make", "Colour"]
door_feature = ["Doors"]
num_features = ["Odometer (KM)"]

# Create an imputer (something that fills missing data)
imputer = ColumnTransformer([
    ("cat_imputer", cat_imputer, cat_features),
    ("door_imputer", door_imputer, door_feature),
    ("num_imputer", num_imputer, num_features)
])

# Fill train and test values separately
filled_x_train = imputer.fit_transform(x_train)
filled_x_test = imputer.transform(x_test)

# Check filled x_train
filled_x_train

# +
# Get our transformed data array's back into DataFrame's
car_sales_filled_train = pd.DataFrame(filled_x_train, 
                                      columns=["Make", "Colour", "Doors", "Odometer (KM)"])

car_sales_filled_test = pd.DataFrame(filled_x_test, 
                                     columns=["Make", "Colour", "Doors", "Odometer (KM)"])

# Check missing data in training set
car_sales_filled_train.isna().sum()
# -

# Check to see the original... still missing values
car_sales_missing.isna().sum()

# +
# Now let's one hot encode the features with the same code as before 
categorical_features = ["Make", "Colour", "Doors"]
one_hot = OneHotEncoder()
transformer = ColumnTransformer([("one_hot", 
                                 one_hot, 
                                 categorical_features)],
                                 remainder="passthrough")

# Fill train and test values separately
transformed_x_train = transformer.fit_transform(car_sales_filled_train)
transformed_x_test = transformer.transform(car_sales_filled_test)

# Check transformed and filled x_train
transformed_x_train.toarray()

# +
# Now we've transformed x, let's see if we can fit a model
np.random.seed(42)
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()

# Make sure to use transformed (filled and one-hot encoded x data)
model.fit(transformed_x_train, y_train)
model.score(transformed_x_test, y_test)
# -


