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

# # Pandas Practice
#
# This notebook is dedicated to practicing different tasks with pandas. The solutions are available in a solutions notebook, however, you should always try to figure them out yourself first.
#
# It should be noted there may be more than one different way to answer a question or complete an exercise.
#
# Exercises are based off (and directly taken from) the quick introduction to pandas notebook.
#
# Different tasks will be detailed by comments or text.
#
# For further reference and resources, it's advised to check out the [pandas documentation](https://pandas.pydata.org/pandas-docs/stable/).

# Import pandas
import pandas as pd

# Create a series of three different colours
colours = pd.Series(["Red", "Green", "Blue"])

# Create a series of three different car types and view it
cars = pd.Series(["Honda", "Skoda", "Mercedes"])

# Combine the Series of cars and colours into a DataFrame
my_df = pd.DataFrame({"Cars": cars, "Colours": colours})

# Import "../data/car-sales.csv" and turn it into a DataFrame
dataframe = pd.read_csv("data/car-sales.csv")
dataframe

# **Note:** Since you've imported `../data/car-sales.csv` as a DataFrame, we'll now refer to this DataFrame as 'the car sales DataFrame'.

# Export the DataFrame you created to a .csv file
my_df.to_csv("data/my_df.csv")

# Find the different datatypes of the car data DataFrame
my_df.dtypes

# Describe your current car sales DataFrame using describe()
my_df.describe()

# Get information about your DataFrame using info()
my_df.info()

# What does it show you?

# Create a Series of different numbers and find the mean of them
numbers = pd.Series([1,2,3,4,5,6])
numbers_mean = numbers.mean()
numbers_mean

# Create a Series of different numbers and find the sum of them
numbers_sum = numbers.sum()
numbers_sum

# List out all the column names of the car sales DataFrame
dataframe.columns

# Find the length of the car sales DataFrame
len(dataframe)

# Show the first 5 rows of the car sales DataFrame
dataframe.head()

# Show the first 7 rows of the car sales DataFrame
dataframe.head(7)

# Show the bottom 5 rows of the car sales DataFrame
dataframe.tail()

# Use .loc to select the row at index 3 of the car sales DataFrame
dataframe.loc[3]

# Use .iloc to select the row at position 3 of the car sales DataFrame
dataframe.iloc[3]

# Notice how they're the same? Why do you think this is? 
#
# Check the pandas documentation for [.loc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html) and [.iloc](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iloc.html). Think about a different situation each could be used for and try them out.

# Select the "Odometer (KM)" column from the car sales DataFrame
dataframe["Odometer (KM)"]

# Find the mean of the "Odometer (KM)" column in the car sales DataFrame
mean_km = dataframe["Odometer (KM)"].mean()
mean_km

# Select the rows with over 100,000 kilometers on the Odometer
dataframe[dataframe["Odometer (KM)"] > 100000 ]

# Create a crosstab of the Make and Doors columns
pd.crosstab(dataframe["Make"], dataframe["Doors"])

# Group columns of the car sales DataFrame by the Make column and find the average
dataframe.groupby(dataframe["Make"]).mean()

# Import Matplotlib and create a plot of the Odometer column
# Don't forget to use %matplotlib inline
import matplotlib.pyplot as plt

# Create a histogram of the Odometer column using hist()
dataframe["Odometer (KM)"].hist()

# Try to plot the Price column using plot()
dataframe["Price"].hist()

# Why didn't it work? Can you think of a solution?
#
# You might want to search for "how to convert a pandas string column to numbers".
#
# And if you're still stuck, check out this [Stack Overflow question and answer on turning a price column into integers](https://stackoverflow.com/questions/44469313/price-column-object-to-int-in-pandas).
#
# See how you can provide the example code there to the problem here.

# Remove the punctuation from price column
dataframe["Price"] = dataframe["Price"].str.replace("$", "")

# Check the changes to the price column
dataframe["Price"]

# Remove the two extra zeros at the end of the price column
dataframe["Price"] = dataframe["Price"].str.removesuffix(".00")

# Check the changes to the Price column
dataframe["Price"] = dataframe["Price"].str.replace(",", "")

# Change the datatype of the Price column to integers
dataframe["Price"] = pd.to_numeric(dataframe["Price"])

# Lower the strings of the Make column
dataframe["Make"] = dataframe["Make"].str.lower()

# If you check the car sales DataFrame, you'll notice the Make column hasn't been lowered.
#
# How could you make these changes permanent?
#
# Try it out.

# Make lowering the case of the Make column permanent
dataframe["Make"]

# Check the car sales DataFrame
dataframe

# Notice how the Make column stays lowered after reassigning.
#
# Now let's deal with missing data.

# +
# Import the car sales DataFrame with missing data ("../data/car-sales-missing-data.csv")

df_missing = pd.read_csv("data/car-sales-missing-data.csv")
# Check out the new DataFrame
df_missing
# -

# Notice the missing values are represented as `NaN` in pandas DataFrames.
#
# Let's try fill them.

# Fill the Odometer column missing values with the mean of the column inplace
df_missing["Odometer"] = df_missing["Odometer"].fillna(df_missing["Odometer"].mean())

# View the car sales missing DataFrame and verify the changes
df_missing

# Remove the rest of the missing data inplace
df_missing.dropna(inplace=True)

# Verify the missing values are removed by viewing the DataFrame
df_missing

# We'll now start to add columns to our DataFrame.

# Create a "Seats" column where every row has a value of 5
dataframe["Seats"] = 5
dataframe

# Create a column called "Engine Size" with random values between 1.3 and 4.5
# Remember: If you're doing it from a Python list, the list has to be the same length
# as the DataFrame
import random
engines = [random.uniform(1.3, 4.5) for i in range(10)]
dataframe["Engine size"] = engines
dataframe

# Create a column which represents the price of a car per kilometer
# Then view the DataFrame
dataframe["Price per KM"] = dataframe["Price"]/dataframe["Odometer (KM)"]
dataframe

# Remove the last column you added using .drop()
dataframe.drop("Price per KM", axis=1, inplace=True)
dataframe

# Shuffle the DataFrame using sample() with the frac parameter set to 1
# Save the the shuffled DataFrame to a new variable
new = dataframe.sample(frac=1)
new

# Notice how the index numbers get moved around. The [`sample()`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sample.html) function is a great way to get random samples from your DataFrame. It's also another great way to shuffle the rows by setting `frac=1`.

# Reset the indexes of the shuffled DataFrame
new.reset_index()

# Notice the index numbers have been changed to have order (start from 0).

# Change the Odometer values from kilometers to miles using a Lambda function
# Then view the DataFrame
dataframe["Odometer (KM)"] = dataframe["Odometer (KM)"]/1.6
dataframe

# +
# Change the title of the Odometer (KM) to represent miles instead of kilometers

dataframe.columns[2].replace("Odometer (KM)", "Odometer (Miles)", inplace)
dataframe
# -

# ## Extensions
#
# For more exercises, check out the pandas documentation, particularly the [10-minutes to pandas section](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html). 
#
# One great exercise would be to retype out the entire section into a Jupyter Notebook of your own.
#
# Get hands-on with the code and see what it does.
#
# The next place you should check out are the [top questions and answers on Stack Overflow for pandas](https://stackoverflow.com/questions/tagged/pandas?sort=MostVotes&edited=true). Often, these contain some of the most useful and common pandas functions. Be sure to play around with the different filters!
#
# Finally, always remember, the best way to learn something new to is try it. Make mistakes. Ask questions, get things wrong, take note of the things you do most often. And don't worry if you keep making the same mistake, pandas has many ways to do the same thing and is a big library. So it'll likely take a while before you get the hang of it.
