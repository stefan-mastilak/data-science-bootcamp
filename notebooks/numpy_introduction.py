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

# #### Pseudo-random arrays
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

# #### Indexing

# Access elements by index:
a3[0]

# #### Slicing

# Access elements by slicing:
a3[0][1:]

a4 = np.random.randint(10. size=(2,3,4,5))


