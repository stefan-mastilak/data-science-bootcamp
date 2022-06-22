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

# # Matplotlib Practice
#
# This notebook offers a set of exercises to different tasks with Matplotlib.
#
# It should be noted there may be more than one different way to answer a question or complete an exercise.
#
# Different tasks will be detailed by comments or text.
#
# For further reference and resources, it's advised to check out the [Matplotlib documentation](https://matplotlib.org/3.1.1/contents.html).
#
# If you're stuck, don't forget, you can always search for a function, for example if you want to create a plot with `plt.subplots()`, search for [`plt.subplots()`](https://www.google.com/search?q=plt.subplots()).

# Import the pyplot module from matplotlib as plt and make sure 
# plots appear in the notebook using '%matplotlib inline'
# %matplotlib inline
import matplotlib.pyplot as plt

# Create a simple plot using plt.plot()
plt.plot()

# Plot a single Python list
plt.plot([1,2,3,4,5])

# Create two lists, one called X, one called y, each with 5 numbers in them
x = [1,2,3,4,5]
y = [6,7,8,9,10]

# Plot X & y (the lists you've created)
plt.plot(x, y)

# There's another way to create plots with Matplotlib, it's known as the object-orientated (OO) method. Let's try it.

# Create a plot using plt.subplots()
fig, ax = plt.subplots()

# Create a plot using plt.subplots() and then add X & y on the axes
fig, ax = plt.subplots()
ax.plot(x,y)

# Now let's try a small matplotlib workflow.

# +
# Import and get matplotlib ready
# %matplotlib inline
import matplotlib.pyplot as plt

# Prepare data (create two lists of 5 numbers, X & y)
x = [11,30,59,70,99]
y = [2,40,65,80,100]

# Setup figure and axes using plt.subplots()
fig, ax = plt.subplots()

# Add data (X, y) to axes
ax.plot(x,y)

# Customize plot by adding a title, xlabel and ylabel
ax.set(xlabel='X', ylabel='Y', title='X and Y plot')

# Save the plot to file using fig.savefig()
# fig.savefig('path_to_save')
# -

# Okay, this is a simple line plot, how about something a little different?
#
# To help us, we'll import NumPy.

# Import NumPy as np
import numpy as np

# Create an array of 100 evenly spaced numbers between 0 and 100 using NumPy and save it to variable X
x = np.linspace(0,10,100)
x

# Create a plot using plt.subplots() and plot X versus X^2 (X squared)
fig, ax = plt.subplots()
ax.plot(x, x**2)

# We'll start with scatter plots.

# Create a scatter plot of X versus the exponential of X (np.exp(X))
fig, ax = plt.subplots()
ax.scatter(x, np.exp(x))

# Create a scatter plot of X versus np.sin(X)
fig, ax = plt.subplots()
ax.scatter(x, np.sin(x))

# How about we try another type of plot? This time let's look at a bar plot. First we'll make some data.

# Create a Python dictionary of 3 of your favourite foods with 
# The keys of the dictionary should be the food name and the values their price
foods = {"pizza": 15, "pasta": 25, "lasagne": 6}

# +
# Create a bar graph where the x-axis is the keys of the dictionary
# and the y-axis is the values of the dictionary
fig, ax = plt.subplots()
ax.bar(foods.keys(), foods.values())

# Add a title, xlabel and ylabel to the plot
ax.set(xlabel='Foods', ylabel='Price', title='Favourite food')
# -

# Make the same plot as above, except this time make the bars go horizontal
fig, ax = plt.subplots()
ax.barh(list(foods.keys()), list(foods.values()))
ax.set(xlabel='Foods', ylabel='Price', title='Favourite food')

# All this food plotting is making me hungry. But we've got a couple of plots to go.
#
# Let's see a histogram.

# +
# Create a random NumPy array of 1000 normally distributed numbers using NumPy and save it to X
x = np.random.randn(1000)

# Create a histogram plot of X
fig, ax = plt.subplots()
ax.hist(x)

# +
# Create a NumPy array of 1000 random numbers and save it to X
x = np.random.rand(1000)

# Create a histogram plot of X
fig, ax = plt.subplots()
ax.hist(x)
# -

# Notice how the distributions (spread of data) are different. Why do they differ? 
#
# What else can you find out about the normal distribution? 
#
# Can you think of any other kinds of data which may be normally distributed?
#
# These questions aren't directly related to plotting or Matplotlib but they're helpful to think of.
#
# Now let's try make some subplots. A subplot is another name for a figure with multiple plots on it.

# Create an empty subplot with 2 rows and 2 columns (4 subplots total)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

# Notice how the subplot has multiple figures. Now let's add data to each axes.

# +
# Create the same plot as above with 2 rows and 2 columns and figsize of (10, 5)
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10,5))

# Plot X versus X/2 on the top left axes
ax1.plot(x,x/2 )


# Plot a scatter plot of 10 random numbers on each axis on the top right subplot
ax2.scatter(np.random.rand(10), np.random.rand(10))

# Plot a bar graph of the favourite food keys and values on the bottom left subplot
ax3.bar(foods.keys(), foods.values())

# Plot a histogram of 1000 random normally distributed numbers on the bottom right subplot
ax4.hist(np.random.randn(1000))
# -

# Woah. There's a lot going on there.
#
# Now we've seen how to plot with Matplotlib and data directly. Let's practice using Matplotlib to plot with pandas.
#
# First we'll need to import pandas and create a DataFrame work with.

# Import pandas as pd


# Import the '../data/car-sales.csv' into a DataFame called car_sales and view


# Try to plot the 'Price' column using the plot() function


# Why doesn't it work?
#
# Hint: It's not numeric data.
#
# In the process of turning it to numeric data, let's create another column which adds the total amount of sales and another one which shows what date the car was sold.
#
# Hint: To add a column up cumulatively, look up the cumsum() function. And to create a column of dates, look up the date_range() function.

# Remove the symbols, the final two numbers from the 'Price' column and convert it to numbers


# +
# Add a column called 'Total Sales' to car_sales which cumulatively adds the 'Price' column


# Add a column called 'Sale Date' which lists a series of successive dates starting from today (your today)

# View the car_sales DataFrame

# -

# Now we've got a numeric column (`Total Sales`) and a dates column (`Sale Date`), let's visualize them.

# Use the plot() function to plot the 'Sale Date' column versus the 'Total Sales' column


# +
# Convert the 'Price' column to the integers


# Create a scatter plot of the 'Odometer (KM)' and 'Price' column using the plot() function


# +
# Create a NumPy array of random numbers of size (10, 4) and save it to X


# Turn the NumPy array X into a DataFrame with columns called ['a', 'b', 'c', 'd']


# Create a bar graph of the DataFrame

# -

# Create a bar graph of the 'Make' and 'Odometer (KM)' columns in the car_sales DataFrame


# Create a histogram of the 'Odometer (KM)' column


# Create a histogram of the 'Price' column with 20 bins


# Now we've seen a few examples of plotting directly from DataFrames using the `car_sales` dataset.
#
# Let's try using a different dataset.

# Import "../data/heart-disease.csv" and save it to the variable "heart_disease"


# View the first 10 rows of the heart_disease DataFrame


# Create a histogram of the "age" column with 50 bins


# Call plot.hist() on the heart_disease DataFrame and toggle the
# "subplots" parameter to True


# That plot looks pretty squished. Let's change the figsize.

# Call the same line of code from above except change the "figsize" parameter
# to be (10, 30)


# Now let's try comparing two variables versus the target variable.
#
# More specifially we'll see how age and cholesterol combined effect the target in **patients over 50 years old**.
#
# For this next challenge, we're going to be replicating the following plot:
#
# <img src="../images/matplotlib-heart-disease-chol-age-plot.png"/>

# +
# Replicate the above plot in whichever way you see fit

# Note: The method below is only one way of doing it, yours might be
# slightly different

# Create DataFrame with patients over 50 years old


# Create the plot


# Plot the data


# Customize the plot


# Add a meanline

# -

# Beatiful, now you've created a plot of two different variables, let's change the style.

# Check what styles are available under plt


# Change the style to use "seaborn-whitegrid"


# Now the style has been changed, we'll replot the same figure from above and see what it looks like.
#
# If you've changed the style correctly, it should look like the following:
# <img src="../images/matplotlib-heart-disease-chol-age-plot-seaborn-whitegrid.png"/>
#

# +
# Reproduce the same figure as above with the "seaborn-whitegrid" style

# Create the plot


# Plot the data


# Customize the plot


# Add a meanline

# -

# Wonderful, you've changed the style of the plots and the figure is looking different but the dots aren't a very good colour.
#
# Let's change the `cmap` parameter of `scatter()` as well as the `color` parameter of `axhline()` to fix it.
#
# Completing this step correctly should result in a figure which looks like this:
# <img src="../images/matplotlib-heart-disease-chol-age-plot-cmap-change.png"/>

# +
# Replot the same figure as above except change the "cmap" parameter
# of scatter() to "winter"
# Also change the "color" parameter of axhline() to "red"

# Create the plot


# Plot the data


# Customize the plot


# Add a meanline

# -

# Beautiful! Now our figure has an upgraded color scheme let's save it to file.

# Save the current figure using savefig(), the file name can be anything you want


# Reset the figure by calling plt.subplots()


# ## Extensions
#
# For more exercises, check out the [Matplotlib tutorials page](https://matplotlib.org/3.1.1/tutorials/index.html). A good practice would be to read through it and for the parts you find interesting, add them into the end of this notebook.
#
# The next place you could go is the [Stack Overflow page for the top questions and answers for Matplotlib](https://stackoverflow.com/questions/tagged/matplotlib?sort=MostVotes&edited=true). Often, you'll find some of the most common and useful Matplotlib functions here. Don't forget to play around with the Stack Overflow filters! You'll likely find something helpful here.
#
# Finally, as always, remember, the best way to learn something new is to try it. And try it relentlessly. Always be asking yourself, "is there a better way this data could be visualized so it's easier to understand?"
