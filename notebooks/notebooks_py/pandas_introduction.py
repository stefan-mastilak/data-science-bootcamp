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

import pandas as pd

# ## Two main datatypes in Pandas:
# 1) Series - one dimensional
# 2) DataFrame - two dimensional

# +
# series - one dimensional
# -

series = pd.Series(["BMW", "Toyota", "Honda"])

colours = pd.Series(["Blue", "Red", "White"])

# +
# dataframe - two dimensional
# -

car_data = pd.DataFrame({"Car make": series, "Colour": colours})

car_data

# +
# import data - instead of creating data by yourself you will probably want to import data from datasource 
# -

car_sales = pd.read_csv("data/car-sales.csv")

car_sales

# +
# exporting a dataframe - to csv, excel, html, json, etc.
# -

car_sales.to_csv("data/exported-car-sales.csv", index=False) # index=False serves well when there is unnamed column in your data

exported_car_sales = pd.read_csv("data/exported-car-sales.csv")

# ## Reading a data from URLs
# Another great feature of pandas is being able to import .csv files directly from a URL.
# For example, for the heart-disease.csv file, using the read_csv() function you can directly import it using the URL from the course GitHub repo:

heart_disease = pd.read_csv("https://raw.githubusercontent.com/mrdbourke/zero-to-mastery-ml/master/data/heart-disease.csv")

# ## Describe data with Pandas

# attribute dtypes - shows data types of the dataframe objects
car_sales.dtypes

# attribute columns - shows dataframe columns
car_sales.columns

# attribute index - shows range of indexes in your dataframe
car_sales.index

# function describe - gives us some statistic info about our data (it works only on numeric columns)
car_sales.describe()

# function info - shows information about the dataframe 
car_sales.info()

# fubnction mean - shows average of numerical columns
car_sales.mean()

# function sum - shows sum of a columns values 
car_sales.sum()
# it's better to call it on the single column
car_sales["Doors"].sum()

# get length of dataframe
len(car_sales)

# dataframe slicing:
car_sales[0:3]

# ## Viewing and selecting data with Pandas

# show first rows of your dataframe
car_sales.head(5) # 5 by default if no value passed in

# shows bottom rows of your dataframe
car_sales.tail() # 5 by default in no value passed in 

# .loc and .iloc
car_sales.loc[3]  # loc stands for location - it shows what is on the index 3

car_sales.iloc[3] # iloc refers to position, not index

car_sales.loc[:3] # shows all the items up to item with index 3 (including)

car_sales["Make"]  # shows 'Make' column

car_sales.Make # shows 'Make' column - second way by accessing attribute

car_sales[car_sales["Make"] == "Toyota"]  # filter on data where Make equals 'Toyota'

car_sales[car_sales["Odometer (KM)"] > 80000] # filter on data where Odometer has more than 80000 km

# ## Comparing data with Pandas

# crosstab - to compare two columns 
pd.crosstab(car_sales["Make"], car_sales["Doors"])

# group by - to compare more than two columns
car_sales.groupby(["Make"]).mean()

# ## Plotting data with Pandas
# Plotting depends on the matplotlib. If it doesn't work try to use those two imports:
#
# # %matplotlib inline
#
# import matplotlib.pyplot as plt

# plot works only on the numeric data 
car_sales["Odometer (KM)"].plot()

# histogram plot
car_sales["Odometer (KM)"].hist()

# to plot price, we need to convert it into the numeric value:
car_sales["Price"] = car_sales["Price"].str.replace("[\$\,\.]", "").astype(int)

car_sales["Price"].plot()

# ## Manipulating data with Pandas

# str.lower - method for lowering letters
car_sales["Make"].str.lower()

# +
# reasigning a values will retain the changes we made 

car_sales["Make"] = car_sales["Make"].str.lower()
car_sales
# -

# ## Missing data 

# missing data - problem that usually occurs in real project
car_sales_missing = pd.read_csv("data/car-sales-missing-data.csv")
car_sales_missing

# +
# in order to fill missing values - use fillna method where you can use mean value calculated from the existing values we have 

car_sales_missing["Odometer"].fillna(car_sales_missing["Odometer"].mean(), inplace=True)  

# inplace=True - will fill up the changes into dataframe, not need to reasign in this case
# -

car_sales_missing

# function dropna - to drop all rows that have some unfilled values within  
car_sales_missing_dropped = car_sales_missing.dropna()

car_sales_missing_dropped

car_sales_missing_dropped.to_csv("data/car-sales-missing-dropped.csv")

# ## Creating columns in Pandas

# +
### Columns from series

seats_col = pd.Series([5,5,5,5,5])
car_sales["Seats"].fillna(5, inplace=True)
car_sales

# +
### Columns from python list - list length must be the same as length of df

fuel_economy = [7.5, 9.2, 5.0, 9.6, 8.7, 7.6, 4.0, 5.5, 9.6, 7.2]
car_sales["Fuel per 100km"] = fuel_economy
car_sales

# +
### Column created from another column

car_sales["Total fuel used"] = car_sales["Odometer (KM)"]/100 * car_sales["Fuel per 100km"]
car_sales

# +
### Create column from a single value

car_sales["4 wheels"] = True
car_sales
# -

# ## Deleting columns in Pandas

car_sales.drop("4 wheels", axis=1, inplace=True)  # axis=1 means column, axis=0 means row
car_sales

# ## Randomizing data order

car_sales

# +
# Shuffling data - order of the rows will be shuffled, not their values 

car_sales_shuffled = car_sales.sample(frac=1)  # frac defines fraction of the data (1 means entire dataframe)
car_sales_shuffled

# +
# to work with only 20% of data use frac=0.2

car_sales_shuffled.sample(frac=0.2)

# +
# to restore from shuffled order use function reset_index()

car_sales_shuffled.reset_index(drop=True, inplace=True)
car_sales_shuffled
# -

# ## Using lambda to apply to a column

# +
# To recalculate Odometer from kilometers to miles we will use apply function:

car_sales["Odometer (KM)"] = car_sales["Odometer (KM)"].apply(lambda x: x/1.6)
car_sales
# -


