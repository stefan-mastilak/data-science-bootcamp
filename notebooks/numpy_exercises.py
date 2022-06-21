# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3
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


# +
# Create a 1-dimensional NumPy array using np.array()


# Create a 2-dimensional NumPy array using np.array()


# Create a 3-dimensional Numpy array using np.array()

# -

# Now we've you've created 3 different arrays, let's find details about them.
#
# Find the shape, number of dimensions, data type, size and type of each array.

# Attributes of 1-dimensional array (shape, 
# number of dimensions, data type, size and type)


# Attributes of 2-dimensional array


# Attributes of 3-dimensional array


# Import pandas and create a DataFrame out of one
# of the arrays you've created


# Create an array of shape (10, 2) with only ones


# Create an array of shape (7, 2, 3) of only zeros


# Create an array within a range of 0 and 100 with step 3


# Create a random array with numbers between 0 and 10 of size (7, 2)


# Create a random array of floats between 0 & 1 of shape (3, 5)


# +
# Set the random seed to 42


# Create a random array of numbers between 0 & 10 of size (4, 6)

# -

# Run the cell above again, what happens?
#
# Are the numbers in the array different or the same? Why do think this is?

# +
# Create an array of random numbers between 1 & 10 of size (3, 7)
# and save it to a variable


# Find the unique numbers in the array you just created

# -

# Find the 0'th index of the latest array you created


# Get the first 2 rows of latest array you created


# Get the first 2 values of the first 2 rows of the latest array


# Create a random array of numbers between 0 & 10 and an array of ones
# both of size (3, 5), save them both to variables


# Add the two arrays together


# Create another array of ones of shape (5, 3)


# Try add the array of ones and the other most recent array together


# When you try the last cell, it produces an error. Why do think this is?
#
# How would you fix it?

# Create another array of ones of shape (3, 5)


# Subtract the new array of ones from the other most recent array


# Multiply the ones array with the latest array


# Take the latest array to the power of 2 using '**'


# Do the same thing with np.square()


# Find the mean of the latest array using np.mean()


# Find the maximum of the latest array using np.max()


# Find the minimum of the latest array using np.min()


# Find the standard deviation of the latest array


# Find the variance of the latest array


# Reshape the latest array to (3, 5, 1)


# Transpose the latest array


# What does the transpose do?

# Create two arrays of random integers between 0 to 10
# one of size (3, 3) the other of size (3, 2)


# Perform a dot product on the two newest arrays you created


# Create two arrays of random integers between 0 to 10
# both of size (4, 3)


# Perform a dot product on the two newest arrays you created


# It doesn't work. How would you fix it?

# Take the latest two arrays, perform a transpose on one of them and then perform 
# a dot product on them both


# Notice how performing a transpose allows the dot product to happen.
#
# Why is this?
#
# Checking out the documentation on [`np.dot()`](https://docs.scipy.org/doc/numpy/reference/generated/numpy.dot.html) may help, as well as reading [Math is Fun's guide on the dot product](https://www.mathsisfun.com/algebra/vectors-dot-product.html).
#
# Let's now compare arrays.

# Create two arrays of random integers between 0 & 10 of the same shape
# and save them to variables


# Compare the two arrays with '>'


# What happens when you compare the arrays with `>`?

# Compare the two arrays with '>='


# Find which elements of the first array are greater than 7


# Which parts of each array are equal? (try using '==')


# Sort one of the arrays you just created in ascending order


# Sort the indexes of one of the arrays you just created


# Find the index with the maximum value in one of the arrays you've created


# Find the index with the minimum value in one of the arrays you've created


# Find the indexes with the maximum values down the 1st axis (axis=1)
# of one of the arrays you created


# Find the indexes with the minimum values across the 0th axis (axis=0)
# of one of the arrays you created


# Create an array of normally distributed random numbers


# Create an array with 10 evenly spaced numbers between 1 and 100


# ## Extensions
#
# For more exercises, check out the [NumPy quickstart tutorial](https://numpy.org/doc/stable/user/quickstart.html). A good practice would be to read through it and for the parts you find interesting, add them into the end of this notebook.
#
# Pay particular attention to the section on broadcasting. And most importantly, get hands-on with the code as much as possible. If in dobut, run the code, see what it does.
#
# The next place you could go is the [Stack Overflow page for the top questions and answers for NumPy](https://stackoverflow.com/questions/tagged/numpy?sort=MostVotes&edited=true). Often, you'll find some of the most common and useful NumPy functions here. Don't forget to play around with the filters! You'll likely find something helpful here.
#
# Finally, as always, remember, the best way to learn something new is to try it. And try it relentlessly. If you get interested in some kind of NumPy function, asking yourself, "I wonder if NumPy could do that?", go and find out.
