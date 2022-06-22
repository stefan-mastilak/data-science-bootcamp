----------------------------------------
Machine learning & Data science Bootcamp
----------------------------------------

## Matplotlib (data visualisation)

* What is Matplotlib
    * Python ploting library
    * Turn date into visualisation
    

* Why Matplotlib?
    * Built on NumPy arrays (and Python)
    * Integrates directly with pandas
    * Can create basic or advanced plots
    * Simple to use interface (once you get the foundations)

```python
# Imports:
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```
```python
# Prepare data:
x = [1,2,3,4]
y = [11,22,33,44]

# Simple plot example:
plt.plot(x, y)

# Setup plot (recommended way):
fig, ax = plt.subplots(figsize=(10,10))
ax.plot(x,y)

# Customize plot:
ax.set(title="Simple plot", xlabel="X", ylabel="Y")

# Save and show:
fig.savefig("images/simple_plot.png")
```

## Anatomy of plot

<img width="998" alt="matplotlib-anatomy-of-a-plot" src="https://user-images.githubusercontent.com/74961891/174809783-da778aa4-d7c9-447b-9804-d33511506b12.png">

<img width="997" alt="matplotlib-anatomy-of-a-plot-with-code" src="https://user-images.githubusercontent.com/74961891/174809910-8d394f58-042a-4782-8eb1-fed97972b3e6.png">


## Making figures with Numpy arrays

* Line plot
* Scatter plot
* Bar plot
* Histogram
* Subplots

```python
# Create some data
x = np.linspace(0,10,100)

# Line plot
fig, ax = plt.subplots()
ax.plot(x, x**2)

# Scatter plot
fig, ax = plt.subplots()
ax.scatter(x, np.exp(x))

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

# Histogram plot 
x = np.random.randn(1000)
fig, ax = plt.subplots()
ax.hist(x)

# Subplot - option 1
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# Plot axes:
ax1.plot(x, x/2)
ax2.scatter(x, x**2)
ax3.bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax4.hist(x)

# Subplot - option 2
fig, ax = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# plot to each different index (list indexing on axes)
ax[0,0].plot(x, x/2)
ax[0,1].scatter(x, x**2)
ax[1,0].bar(nut_butter_prices.keys(), nut_butter_prices.values())
ax[1,1].hist(x)
```

## Plotting from Pandas dataframes

```python
# Make a dataframe
car_sales = pd.read_csv("data/car-sales.csv")
car_sales


# Format car_sales dataframe:

# 1) replace dollar sign from price and remove dot and comma fro the price 
car_sales["Price"] = car_sales["Price"].str.replace('[\$\,\.]', '')

# 2) remove last two zeros from car price
car_sales["Price"] = car_sales["Price"].str[:-2]

# 3) add Sale date column to dataframe
car_sales["Sale Date"] = pd.date_range('1/1/2022', periods=len(car_sales))

# 4) add Total colum to sum s
car_sales["Total sales"] = car_sales["Price"].astype(int).cumsum()


# Let's plot the total sales from car_sales dataframe:
car_sales.plot(x="Sale Date", y="Total sales")

# Scatter plot from car_sales dataframe
car_sales.plot(x="Odometer (KM)", y="Price", kind="scatter")

# Bar plot from car_sales dataframe
car_sales.plot(x="Make", y="Odometer (KM)", kind='bar')

# Bar plot from Pandas dataframe
x = np.random.rand(10,4)
df = pd.DataFrame(x, columns=['a','b','c','d'])
df.plot.bar()   # equivalent to: df.plot(kind="bar")


```
