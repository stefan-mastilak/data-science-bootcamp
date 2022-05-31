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

# Import numpy
import numpy as np

# ## Datatypes and attributes
#

# +
# Numpy's main datatype is ndarray - (n-dimensional array)

# Shape (1,3) - 1 row, 3 columns - one dimension array (vector)
a1 = np.array([1,2,3])

# Shape (2,3) - 1 rows, 3 columns - two dimensional array (matrix)
a2 = np.array([[1,2,3], [4,6.5,7]])

# Shape (3,3,2) - 3 rows, 3 columns, 2 layers - three dimensional array (matrix)
a3 = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[10,11,12],[13,14,15],[16,17,18]]])
# -

# Show shape of array:
a3.shape

# Show number of dimensions of our arrays:
a1.ndim, a2.ndim, a3.ndim

# Show datatypes of our arrays:
a1.dtype, a2.dtype, a3.dtype

# Show number of elements in arrays:
a1.size, a2.size, a3.size

# ## Creating arrays

# Create a Pandas DataFrame from numpy array
import pandas as pd
df = pd.DataFrame(a2)

# Creating numpy array:
sample_array = np.array([1,2,3])
sample_array

# #### ones()

# ones() function will return a new array of given shape and type filled with ones
ones = np.ones(shape=(2,3), dtype=int)
ones

# #### zeroes()

# zeroes() function will return a new array of given shape and type filled with zeros
zeros = np.zeros(shape=(2,3), dtype=float)
zeros

# #### arrange()

# arrange() function to create array from range like start-stop-step
range_array = np.arange(0,10,2)
range_array

# #### random.randint()

# random array using random.randint() function to create integers in range from low to high
random_array = np.random.randint(low=0, high=10, size=(3,5))
random_array

# #### random.random()

# random array using random.random() function to create floats in the half-open interval from 0 to 1
random_array2 = np.random.random((2,3))
random_array2

# #### random.rand()

# random array using random.rand() function to create random values in the given shape
random_array3 = np.random.rand(2,3)
random_array3

# ### Pseudo-random arrays
# #### random.seed()

# Pseudo-random arrays - allows us to create random arrays that are reproducable 
# line below ensures that our random_array4 will be the same no matter how many times we will run this command :) 
np.random.seed(seed=0)
random_array4 = np.random.randint(10, size=(5,3))
random_array4

np.random.seed(seed=7)
random_array5 = np.random.random((5,3))
random_array5

# ## Viewing arrays and matrices

# Get unique elements of array:
np.unique(random_array4)

a3

# ### Indexing

# Access elements by index:
a3[0]

# ### Slicing

# Access elements by slicing:
a3[0][1:]

a4 = np.random.randint(10, size=(2,3,4,5))
a4

a4.shape, a4.ndim

# Get the first 4 elements of the inner most array:
a4[:, :, :, :4]

# ## Manipulating and comparing arrays 

# ### Arithmetic operations

a1

a2

ones = np.ones(3)
ones

# Adding two arrays - elements will be summed 
a1 + ones

# Subtraction of array elements
a1 - ones

# Multiplication of array elements:
a1 * ones

# Floor division (removes decimals by rounding down)
a2 // a1

# Square
a1 ** 2

# Modulo
a1 % 2

# Exponential
np.exp(a1)

# Logarithm
np.log(a1)

# ### Reshaping

# +
# NOTE: Check numpy broadcasting to see how arithmetic operations behave on arrays with different shapes
# https://numpy.org/doc/stable/user/basics.broadcasting.html
# -

a2

a3

# How can you reshape a2 to be compatible with a3?
a2 * a3

a2.shape, a3.shape

a2.reshape(2,3,1).shape

a3.shape

a2_reshaped = a2.reshape(2,3,1)

a2_reshaped * a3

# ### Transposing

# +
# Transpose = switches the axis'
# -

a2

# Transpose array a2:
a2.T

a2.T.shape

# ### Aggregation 

# Aggregation = performing the same operation on a number of things
#
# NOTE: Use python's methods (`sum()`) on Python datatypes
#
# NOTE: Use Numpy's methods (`np.sum()`) on Numpy arrays

# Create massive numpy array:
massive_arr = np.random.random(100000)
massive_arr.size

# Compare Python's sum and Numpy's sum methods performance:
# %timeit sum(massive_arr)
# %timeit np.sum(massive_arr)

# +
# As you can see numpy is more than 500 times faster. It's because Numpy is optimized to perform numerical calculations
# -

a2

# Sum
np.sum(a2)

# Mean
np.mean(a2)

# Max
np.max(a2)

# Min
np.min(a2)

# ### Standard deviation and Variance

# Standard deviation = measure of how spread out a group of numbers is from the mean
np.std(a2)

# Variance = measure of the average degree to which each number is different to the mean
# Higher variance = wider ange of numbers
# Lower variance = lower range of numbers
np.var(a2)

# Standard deviation = squareroot of variance:
np.sqrt(np.var(a2))

# Demo of std and var
high_var_arr = np.array([1, 100, 200, 4000, 5000])
low_var_arr = np.array([2, 4, 6, 8, 10])

np.var(high_var_arr)

np.var(low_var_arr)

np.std(high_var_arr)

np.std(low_var_arr)

np.mean(high_var_arr)

np.mean(low_var_arr)

# +
# %matplotlib inline
import matplotlib.pyplot as plt

plt.hist(high_var_arr)
plt.show()
# -

plt.hist(low_var_arr)
plt.show()

# ### Dot product
# ##### Dot product is just another way of finding patterns between two different sets of numbers

# +
np.random.seed()

mat1 = np.random.randint(10, size=(5, 3))
mat2 = np.random.randint(10, size=(5, 3))
# -

mat1

mat2

# Element-wise multiplication:
mat1 * mat2

# Dot product multiplication:
np.dot(mat1, mat2)

# +
# NOTE: It's not working because shapes (5,3) (5,3) are not aligned - meaning Numbers on the inside must match. 
# Meaning we need to have shapes like (5,3) and (3,5)

# NOTE: check http://matrixmultiplication.xyz/
# Solution: use transpose on matrix to solve it
# -

np.dot(mat1,mat2.T)

# ### Dot product usage example

np.random.seed(0)
sales_amounts = np.random.randint(20, size=(5,3))
sales_amounts

# Create weekly sales DataFrame
import pandas as pd
weekly_sales = pd.DataFrame(sales_amounts, index=["Mon", "Tue", "Wed", "Thu", "Fri"], 
                            columns=["Almond butter", "Peanut butter", "Cashew butter"])
weekly_sales

# Create prices array:
prices = np.array([10,8,12])
prices

# Create butter_prices DataFrame:
butter_prices = pd.DataFrame(prices.reshape(1,3), index=["Price"], columns=["Almond butter", "Peanut butter", "Cashew butter"])
butter_prices

total_sales = prices.dot(sales_amounts)

# Shapes aren't aligned - transpose needed
total_sales = prices.dot(sales_amounts.T)
total_sales

# Create daily sales:
butter_prices.shape, weekly_sales.shape

# Create daily sales:
daily_sales = butter_prices.dot(weekly_sales.T)
daily_sales

# Put that column to the table weekly sales:
weekly_sales["Total ($)"] = daily_sales.T
weekly_sales

# ### Comparison operators
# ##### Basic comparison operator for numpy arrays

a1

a2

# More than:
a1 > a2

# Less than:
a1 < a2

# More or equal:
a1 >= a2

# Less or equal:
a1 <= a2

# Equality:
a1 == a2

# Unequality
a1 != a2

# # Sorting arrays

random_array

random_array.shape

# Sort numbers on each axis of array:
np.sort(random_array)

# Sorting based on indexes of numbers in array:
np.argsort(random_array)

# argmin - Returns the indices of the minimum values along an axis
np.argmin(random_array, axis=0)

# arxmax - Returns the indices of the maximum values along an axis
np.argmax(random_array, axis=0)

# ## Example - Turn Images into Numpy arrays

# + language="html"
# <img src="images/numpy-panda.png" />
# -


