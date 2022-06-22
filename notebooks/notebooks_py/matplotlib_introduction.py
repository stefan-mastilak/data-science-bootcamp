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

# # Indtoruction to Matplotlib

# ### Plot example workflow

# +
# Imports:

# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# +
# Prepare some data:

x = [1,2,3,4]
y = [11,22,3,44]

# Simple plot:
plt.plot(x, y)

# +
# Prepare plot (recommended way):

fig, ax = plt.subplots(figsize=(6,6))
ax.plot(x,y)
# -

type(fig), type(ax)

# +
# Customize plot:

ax.set(title="Simple plot", xlabel="X", ylabel="Y")

# +
# Save and show:

fig.savefig("images/simple_plot.png")
# -

# ## Making figures with Numpy arrays
#
# * Line plot
# * Scatter plot
# * Bar plot
# * Histogram
# * Subplots

import numpy as np

# Create some data
x = np.linspace(0,10,100)
x

# #### Line plot

# Line plot
fig, ax = plt.subplots()
ax.plot(x, x**2)

# #### Scatter plot

# Scatter plot
fig, ax = plt.subplots()
ax.scatter(x, np.exp(x))

# #### Bar plot

# Bar plot
# Let's do a plot from dictionary
nut_butter_prices = {"peanut butter": 10, 
                    "almond butter": 8,
                    "cashew butter": 12}
fig, ax = plt.subplots()
ax.bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax.set(title="Nut butter store prices",ylabel="Price ($)")

# Bar plot - horizontal
fig, ax = plt.subplots()
ax.barh(list(nut_butter_prices.keys()), list(nut_butter_prices.values()))

# #### Histogram plot

# Make some data for histogram and plot it
x = np.random.randn(1000)
fig, ax = plt.subplots()
ax.hist(x)

# #### Subplots - Option 1

# +
# Option 1
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# Plot different axes:
ax1.plot(x, x/2)
ax2.scatter(x, x**2)
ax3.bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax4.hist(x)
# -

# #### Subplots - Option 2

# +
# Option 2
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# plot to each different index (list indexing on axes)
ax[0,0].plot(x, x/2)
ax[0,1].scatter(x, x**2)
ax[1,0].bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax[1,1].hist(x)
# -

# ## Plotting from Pandas dataframes

# Make a dataframe
car_sales = pd.read_csv("data/car-sales.csv")
car_sales

# +
# format car_sales dataframe:

# 1) replace dollar sign from price and remove dot and comma fro the price 
car_sales["Price"] = car_sales["Price"].str.replace('[\$\,\.]', '')

# 2) remove last two zeros from car price
car_sales["Price"] = car_sales["Price"].str[:-2]

# 3) add Sale date column to dataframe
car_sales["Sale Date"] = pd.date_range('1/1/2022', periods=len(car_sales))

# 4) add Total colum to sum s
car_sales["Total sales"] = car_sales["Price"].astype(int).cumsum()

# -

car_sales

# Let's plot the total sales:
car_sales.plot(x="Sale Date", y="Total sales")

# Scatter plot from car_sales dataframe
car_sales.plot(x="Odometer (KM)", y="Price", kind="scatter")

# Bar plot from Pandas dataframe
x = np.random.rand(10,4)
df = pd.DataFrame(x, columns=['a','b','c','d'])
df

df.plot.bar()

# Bar plot from car_sales dataframe
car_sales.plot(x="Make", y="Odometer (KM)", kind='bar')

# Histogram plot from car_sales dataframe
car_sales["Odometer (KM)"].plot.hist()

car_sales["Odometer (KM)"].plot.hist(bins=20)

# Let's try on the heart disease dataset:
heart_disease = pd.read_csv("data/heart-disease.csv")
heart_disease.head()

# Create histogram on heart disease dataframe based on age
heart_disease["age"].plot.hist(bins=20)

heart_disease.plot.hist(figsize=(10,20), subplots=True)


