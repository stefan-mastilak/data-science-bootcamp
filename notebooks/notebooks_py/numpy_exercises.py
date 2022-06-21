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

# # NumPy Practice
#
# This notebook offers a set of exercises for different tasks with NumPy.
#
# It should be noted there may be more than one different way to answer a question or complete an exercise.
#
# Exercises are based off (and directly taken from) the quick introduction to NumPy notebook.
#
# Different tasks will be detailed by comments or text.
#
# For further reference and resources, it's advised to check out the [NumPy documentation](https://numpy.org/devdocs/user/index.html).
#
# And if you get stuck, try searching for a question in the following format: "how to do XYZ with numpy", where XYZ is the function you want to leverage from NumPy.

# Import NumPy as its abbreviation 'np'
import numpy as np

# +
# Create a 1-dimensional NumPy array using np.array()
one_dim = np.array([1,2,3])

# Create a 2-dimensional NumPy array using np.array()
two_dim = np.array([[1,2,3],[4,5,6]])

# Create a 3-dimensional Numpy array using np.array()
three_dim = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[10,11,12],[13,14,15],[16,17,18]]])

# print arrays:
one_dim, two_dim, three_dim
# -

# Now we've you've created 3 different arrays, let's find details about them.
#
# Find the shape, number of dimensions, data type, size and type of each array.

# +
# Attributes of 1-dimensional array (shape, 
# number of dimensions, data type, size and type)

one_dim.shape, one_dim.ndim, type(one_dim), one_dim.size

# +
# Attributes of 2-dimensional array

two_dim.shape, two_dim.ndim, type(two_dim), two_dim.size

# +
# Attributes of 3-dimensional array

three_dim.shape, three_dim.ndim, type(three_dim), three_dim.size

# +
# Import pandas and create a DataFrame out of one
# of the arrays you've created

import pandas as pd

df = pd.DataFrame(two_dim)
df
# -

# Create an array of shape (10, 2) with only ones
ones = np.ones(shape=(10,2))
ones

# Create an array of shape (7, 2, 3) of only zeros
zeros = np.zeros(shape=(7,2,3))
zeros

# Create an array within a range of 0 and 100 with step 3
ranged = np.arange(0,100,3)
ranged

# Create a random array with numbers between 0 and 10 of size (7, 2)
randomized = np.random.randint(0,10,(7,2))
randomized

# Create a random array of floats between 0 & 1 of shape (3, 5)
randfloat = np.random.random((3,5))
randfloat

# +
# Set the random seed to 42
seeded = np.random.seed(42)

# Create a random array of numbers between 0 & 10 of size (4, 6)
seededrand = np.random.randint(0,10, (4,6))
seededrand
# -

# Run the cell above again, what happens?
#
# Are the numbers in the array different or the same? Why do think this is?

# Create an array of random numbers between 1 & 10 of size (3, 7)
# and save it to a variable
var = np.random.randint(0,10, (3,7))
var

# Find the unique numbers in the array you just created
np.unique(var)

# Find the 0'th index of the latest array you created
var[0]

# Get the first 2 rows of latest array you created
var[:2]

# Get the first 2 values of the first 2 rows of the latest array
var[:2, :2]

# +
# Create a random array of numbers between 0 & 10 and an array of ones
# both of size (3, 5), save them both to variables
var1 = np.random.randint(0,10,(3,5))
var2 = np.ones((3,5))

var1, var2

# +
# Add the two arrays together
added1 = var1 + var2
added1

added2 = np.add(var1, var2) # second option :)
added2
# -

# Create another array of ones of shape (5, 3)
ones2 = np.ones((5,3))
ones2

# Try add the array of ones and the other most recent array together
added2 + ones2.transpose()

# When you try the last cell, it produces an error. Why do think this is?
#
# How would you fix it?

# +
# Create another array of ones of shape (3, 5)
# Fixed in previous exercise by transposing array to the same shapes

# +
# Subtract the new array of ones from the other most recent array
# Fixed in previous exercise by transposing array to the same shapes
# -

# Multiply the ones array with the latest array
multiplied = added2 * ones2.transpose()
multiplied

# Take the latest array to the power of 2 using '**'
added2 ** 2

# Do the same thing with np.square()
np.square(added2)

# Find the mean of the latest array using np.mean()
np.mean(added2)

# Find the maximum of the latest array using np.max()
np.max(added2)

# Find the minimum of the latest array using np.min()
np.min(added2)

# Find the standard deviation of the latest array
np.std(added2)

# Find the variance of the latest array
np.var(added2)

# Reshape the latest array to (3, 5, 1)
a2reshaped = added2.reshape(3,5,1)
a2reshaped

# Transpose the latest array
a2transposed = a2reshaped.transpose()
a2transposed

# What does the transpose do?

# +
# Create two arrays of random integers between 0 to 10
# one of size (3, 3) the other of size (3, 2)
r1 = np.random.randint(0,10,(3,3))
r2 = np.random.randint(0,10,(3,2))

r1.shape, r2.shape
# -

# show arrays: 
r1, r2

# Perform a dot product on the two newest arrays you created
np.dot(r1, r2)

# +
# Create two arrays of random integers between 0 to 10
# both of size (4, 3)
r3 = np.random.randint(0,10,(4,3))
r4 = np.random.randint(0,10,(4,3))

r3.shape, r4.shape
# -

# Perform a dot product on the two newest arrays you created
np.dot(r3, r4.transpose())

# It doesn't work. How would you fix it?

# +
# Take the latest two arrays, perform a transpose on one of them and then perform 
# a dot product on them both
# Solved by transposing second array in previous exercise
# -

# Notice how performing a transpose allows the dot product to happen.
#
# Why is this?
#
# Checking out the documentation on [`np.dot()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html) may help, as well as reading [Math is Fun's guide on the dot product](https://www.mathsisfun.com/algebra/vectors-dot-product.html).
#
# Let's now compare arrays.

# +
# Create two arrays of random integers between 0 & 10 of the same shape
# and save them to variables
r5 = np.random.randint(0,10,(3,3))
r6 = np.random.randint(0,10,(3,3))

r5.shape, r6.shape
# -

# show arrays:
r5, r6

# Compare the two arrays with '>'
r5 > r6

# What happens when you compare the arrays with `>`?

# Compare the two arrays with '>='
r5 >= r6

# Find which elements of the first array are greater than 7
r6[r6 > 7]

# Which parts of each array are equal? (try using '==')
(r5==r6).all()

# Sort one of the arrays you just created in ascending order
r6.sort()
r6

# Sort the indexes of one of the arrays you just created
r6.argsort()

# Find the index with the maximum value in one of the arrays you've created
r6.argmax()

# Find the index with the minimum value in one of the arrays you've created
r6.argmin()

# Find the indexes with the maximum values down the 1st axis (axis=1)
# of one of the arrays you created
r6.argmax(axis=1)

# Find the indexes with the minimum values across the 0th axis (axis=0)
# of one of the arrays you created
r6.argmin(axis=0)

# Create an array of normally distributed random numbers
nds = np.random.normal(size=(3,3))
nds

# Create an array with 10 evenly spaced numbers between 1 and 100
spaced = np.linspace(1, 100, 10)
spaced

# ## Extensions
#
# For more exercises, check out the [NumPy quickstart tutorial](https://numpy.org/doc/stable/user/quickstart.html). A good practice would be to read through it and for the parts you find interesting, add them into the end of this notebook.
#
# Pay particular attention to the section on broadcasting. And most importantly, get hands-on with the code as much as possible. If in dobut, run the code, see what it does.
#
# The next place you could go is the [Stack Overflow page for the top questions and answers for NumPy](https://stackoverflow.com/questions/tagged/numpy?sort=MostVotes&edited=true). Often, you'll find some of the most common and useful NumPy functions here. Don't forget to play around with the filters! You'll likely find something helpful here.
#
# Finally, as always, remember, the best way to learn something new is to try it. And try it relentlessly. If you get interested in some kind of NumPy function, asking yourself, "I wonder if NumPy could do that?", go and find out.
