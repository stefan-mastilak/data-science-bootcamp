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

# 4) add Total column to sum sales
car_sales["Total sales"] = car_sales["Price"].astype(int).cumsum()


# Plot the total sales from car_sales dataframe:
car_sales.plot(x="Sale Date", y="Total sales")

# Scatter plot from car_sales dataframe:
car_sales.plot(x="Odometer (KM)", y="Price", kind="scatter")

# Bar plot from car_sales dataframe:
car_sales.plot(x="Make", y="Odometer (KM)", kind='bar')

# Histogram plot from car_sales dataframe:
car_sales["Odometer (KM)"].plot.hist(bins=10)
```

### Which plot to use? Pyplot vs matplotlib Object Oriented methods

* When plotting something quickly - use pyplot methods
* When plotting something advanced - use matplotlib OO methods

```python
# heart disease dataset:
heart_disease = pd.read_csv("data/heart-disease.csv")

# get records with age over 50
over_50 = heart_disease[heart_disease["age"] > 50]

# 1) Pyplot method:
    over_50.plot(kind="scatter", x='age', y='chol', c="target")

# 2) Matplotlib Object Oriented method

    # a) Matplotlib OO method mixed with pyplot:
    fig, ax = plt.subplots(figsize=(10,6))
    over_50.plot(kind="scatter", x='age', y='chol', c="target", ax=ax)
    
    # OO method from scratch
    fig, ax = plt.subplots(figsize=(10,6))
    
    # plot the data:
    scatter = ax.scatter(x=over_50["age"], y=over_50["chol"], c=over_50['target'])
    
    # customize the plot:
    ax.set(title="Heart disease and cholesterol levels",
          xlabel="Age",
          ylabel="Cholesterol")
    
    # add a legend
    ax.legend(*scatter.legend_elements(), title="Target")
    
    # add a horizontal line to show mean value of cholesterol:
    ax.axhline(over_50["chol"].mean(), linestyle='--')
  ```

```python
# Subplot of cholesterol, age, and thalach (max hearth rate)

fig, (ax0, ax1) = plt.subplots(figsize=(10,10), 
                               nrows=2, 
                               ncols=1)

# add data to axis 0:
scatter0 = ax0.scatter(x=over_50['age'], 
                       y=over_50['chol'], 
                       c=over_50['target'])

# customize axis 0:
ax0.set(title="heart Disease and Colesterol levels", 
        xlabel='Age', 
        ylabel='Cholesterol')

# add legend to axis 0:
ax0.legend(*scatter0.legend_elements(), 
           title="Target")

# add a meanline to axis 0;
ax0.axhline(y=over_50['chol'].mean(), 
            linestyle='--')

# add data to axis 1:
scatter1 = ax1.scatter(x=over_50['age'], 
                       y=over_50['thalach'], 
                       c=over_50['target'])

# customize axis 1:
ax1.set(title='Hear Disease and Max hearth rate', 
        xlabel='Age', 
        ylabel='Thalach')

# add legend to axis 1:
ax1.legend(*scatter1.legend_elements(), 
           title="Target")

# add a meanline to axis 1;
ax1.axhline(y=over_50['thalach'].mean(), 
            linestyle='--')

# add title to the figure:
fig.suptitle(t="Heart disease analysis", 
             fontsize=16, 
             fontweight='bold')
```

### Styling the plot

```python
# To see the different styles available:
plt.style.available

# update style to seaborn-whitegrid
plt.style.use("seaborn-whitegrid")

# plot data - new style will be applied:
car_sales['Odometer (KM)'].plot()



# How to change style within oo matplotlib methods?
plt.style.use("seaborn-whitegrid")

fig, ax = plt.subplots(figsize=(10,6))

# plot the data:
scatter = ax.scatter(x=over_50["age"], 
                     y=over_50["chol"], 
                     c=over_50['target'],
                     cmap='winter')  # change the color schema 

# customize the plot:
ax.set(title="Heart disease and cholesterol levels",
      xlabel="Age",
      ylabel="Cholesterol")

# add a legend
ax.legend(*scatter.legend_elements(), title="Target")

# add a horizontal line to show mean value of cholesterol:
ax.axhline(over_50["chol"].mean(), linestyle='--')
```

### Customizing x and y axis limitations:

```python
# Subplot of cholesterol, age, and thalach

fig, (ax0, ax1) = plt.subplots(figsize=(10,10), nrows=2, ncols=1)

# add data to axis 0:
scatter0 = ax0.scatter(x=over_50['age'], 
                       y=over_50['chol'], 
                       c=over_50['target'],
                       cmap='winter')

# customize axis 0:
ax0.set(title="heart Disease and Colesterol levels", 
        xlabel='Age', 
        ylabel='Cholesterol')

# set limit for x:
ax0.set_xlim([50, 80])

# add legend to axis 0:
ax0.legend(*scatter0.legend_elements(), 
           title="Target")

# add a meanline to axis 0;
ax0.axhline(y=over_50['chol'].mean(), 
            linestyle='--')

# add data to axis 1:
scatter1 = ax1.scatter(x=over_50['age'], 
                       y=over_50['thalach'], 
                       c=over_50['target'],
                       cmap='winter')

# customize axis 1:
ax1.set(title='Hear Disease and Max hearth rate', 
        xlabel='Age', 
        ylabel='Thalach')

# set limit for x and y axis:
ax1.set_xlim([50, 80])
ax1.set_ylim([50, 200])

# add legend to axis 1:
ax1.legend(*scatter1.legend_elements(), 
           title="Target")

# add a meanline to axis 1;
ax1.axhline(y=over_50['thalach'].mean(), 
            linestyle='--')

# add title to the figure:
fig.suptitle(t="Heart disease analysis", 
             fontsize=16, 
             fontweight='bold')
```

![my_plot](https://user-images.githubusercontent.com/74961891/175033657-8919396f-2e06-4f06-9484-71bd4ac434cf.png)

### Saving and sharing the plots

```python
# to export your figure use:
fig.savefig("images/my_plot")
```
