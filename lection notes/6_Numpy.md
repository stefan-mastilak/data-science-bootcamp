----------------------------------------
Machine learning & Data science Bootcamp
----------------------------------------

## Numpy

   * Numpy is a Python package written in C
   * Numpy is used to perform numerical operations and for processing n-dimensional arrays

```python
# Import numpy
import numpy as np
```

   * Differences against Pandas:
      * Numpy majorly works with numerical data whereas Pandas works with tabular data
      * Numpy consumes less memory as compared to Pandas
      * Pandas dataframe is used to store a structured dataset. It is more like a spreadsheet than an array
      * NumPy array is just an array of numbers
      
![corrected](https://user-images.githubusercontent.com/74961891/169285813-a9ada68a-3a51-4e05-ad72-78795149791a.png)
 
### Data types and attributes (ndarray)

   * Numpy's main datatype is ndarray (n-dimensional array)

```python
import numpy as np

# Shape (1,3) - 1 row, 3 columns - one dimension array (vector)
a1 = np.array([1,2,3])

# Shape (2,3) - 1 rows, 3 columns - two dimensional array (matrix)
a2 = np.array([[1,2,3], [4,6.5,7]])

# Shape (2,3,3) - 2 layers, 3 rows, 3 columns - three dimensional array (matrix)
a3 = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[10,11,12],[13,14,15],[16,17,18]]])


# Show shape of array:
a3.shape
# console:
(2, 3, 3)


# Show number of dimensions of our arrays:
a1.ndim, a2.ndim, a3.ndim
# console:
(1, 2, 3)


# Show datatypes of our arrays:
a1.dtype, a2.dtype, a3.dtype
# console:
(dtype('int32'), dtype('float64'), dtype('int32'))


# Show number of elements in arrays:
a1.size, a2.size, a3.size
# console:
(3, 6, 18)


# Create a Pandas DataFrame from numpy array 
import pandas as pd
a2 = np.array([[1,2,3], [4,6.5,7]])
df = pd.DataFrame(a2)
```


### Creating arrays
Numpy functions to be used:

   * Placeholder arrays:
     * ones()
     * zeros()
        

   * Range array:
     * arrange()
   

   * Random array:
     * random.randint()
     * random.random()
     * random.rand()
     

   * Pseudo-random array:
     * random.seed()
     
```python
import numpy as np

# Creating numpy array:
sample_array = np.array([1,2,3])


# ones() function will return a new array of given shape and type filled with ones
ones = np.ones(shape=(2,3), dtype=int)
ones
# console:
array([[1, 1, 1], 
       [1, 1, 1]])


# zeroes() function will return a new array of given shape and type filled with zeros
zeros = np.zeros(shape=(2,3), dtype=float)
zeros
# console:
array([[0., 0., 0.], 
       [0., 0., 0.]])


# arrange() function to create array from range like: start-stop-step
range_array = np.arange(0,10,2)
range_array
# console:
array([0, 2, 4, 6, 8])


# random array using random.randint() function to create integers in range from low to high
random_array = np.random.randint(low=0, high=10, size=(3,5))
random_array
# console:
array([[7, 4, 4, 7, 0], 
       [0, 0, 9, 5, 7], 
       [7, 8, 3, 9, 1]])


# random array using random.random() function to create floats in the half-open interval from 0 to 1
random_array2 = np.random.random((2,3))
random_array2
# console:
array([[0.90025663, 0.22956566, 0.94998119], 
       [0.17103584, 0.86062334, 0.20246913]])


# random array using random.rand() function to create random values in the given shape
random_array3 = np.random.rand(2,3)
random_array3
# console:
array([[0.68284128, 0.48876519, 0.79986118], 
       [0.86774647, 0.13287731, 0.5262673 ]])


# Pseudo-random arrays - allows us to create random arrays that are reproducable 
# line below ensures that our random_array4 will be the same no matter how many times we will run this command :) 
np.random.seed(seed=0)
random_array4 = np.random.randint(10, size=(5,3))
random_array4
```

### Viewing arrays and matrices
Functions to be used:

 * unique() - get unique elements of the array
 * indexing - access by list index
 * slicing - access by list slicing

```python
# Access elements by index:
a3[0]
# console:
array([[1, 2, 3], 
       [4, 5, 6], 
       [7, 8, 9]])


# Access elements by slicing:
a3[0][1:]
# console:
array([[4, 5, 6], 
       [7, 8, 9]])

```

### Manipulating and comparing arrays

#### Arithmetic operations
* Check numpy broadcasting to see how arithmetic operations behave on arrays with different shapes.
  The term broadcasting describes how NumPy treats arrays with different shapes during arithmetic operations. 
  Subject to certain constraints, the smaller array is “broadcast” across the larger array so that they have 
  compatible shapes
* https://numpy.org/doc/stable/user/basics.broadcasting.html

```python
a1
# console:
array([1, 2, 3])

a2
# console:
array([[1. , 2. , 3. ], 
       [4. , 6.5, 7. ]])

ones
# console:
array([1., 1., 1.])


# Adding two arrays - elements will be summed 
a1 + ones
# console:
array([2., 3., 4.])


# Subtraction of array elements
a1 - ones
# console:
array([0., 1., 2.])


# Multiplication of array elements:
a1 * ones
# console:
array([1., 2., 3.])


# Floor division (removes decimals by rounding down)
a2 // a1
# console:
array([[1., 1., 1.], 
       [4., 3., 2.]])


# Square
a1 ** 2
# console:
array([1, 4, 9])


# Modulo
a1 % 2
# console:
array([1, 0, 1], dtype=int32)


# Exponential
np.exp(a1)
# console:
array([ 2.71828183,  7.3890561 , 20.08553692])


# Logarithm
np.log(a1)
# console:
array([0. , 0.69314718, 1.09861229])
```
#### Aggregation
* Aggregation = performing the same operation on a number of things
* Note: Use python's methods (sum()) on Python datatypes
* Note: Use Numpy's methods (np.sum()) on Numpy arrays

```python
# Create massive numpy array:
massive_arr = np.random.random(100000)
massive_arr.size
# console >> 100000

# Compare Python's sum and Numpy's sum methods performance:
%timeit sum(massive_arr)
%timeit np.sum(massive_arr)
# console >> 6.3 ms ± 47.9 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# console >> 37 µs ± 222 ns per loop (mean ± std. dev. of 7 runs, 10,000 loops each)
# Note: As you can see numpy is more than 500 times faster because Numpy is optimized to perform numerical calculations

a2
# console:
array([[1. , 2. , 3. ], 
       [4. , 6.5, 7. ]])

# Sum
np.sum(a2)
# console:
23.5


# Mean
np.mean(a2)
# console:
3.916


# Max
np.max(a2)
# console:
7.0


# Min
np.min(a2)
# console:
1.0
```
#### Standard deviation and Variance

* Standard deviation = measure of how spread out a group of numbers is from the mean
* Variance = measure of the average degree to which each number is different to the mean

```python
# Standard deviation = measure of how spread out a group of numbers is from the mean
np.std(a2)
# console >> 2.206

# Variance = measure of the average degree to which each number is different to the mean
# Higher variance = wider ange of numbers
# Lower variance = lower range of numbers
np.var(a2)
# console >> 4.868

# Standard deviation = squareroot of variance:
np.sqrt(np.var(a2))
# console >> 2.206

# Demo of std and var
high_var_arr = np.array([1, 100, 200, 4000, 5000])
low_var_aee = np.array([2, 4, 6, 8, 10])

np.var(high_var_arr)
# console >> 4749656.16

np.var(low_var_arr)
# console >> 8.0

np.std(high_var_arr)
# console >> 2179.37

np.std(low_var_arr)
# console >> 2.82

np.mean(high_var_arr)
# console >> 1860.2

np.mean(low_var_arr)
# console >> 6.0
```

#### Reshaping

* Numpy broadcasting: https://numpy.org/doc/stable/user/basics.broadcasting.html
* When operating on two arrays NumPy compares their shapes element-wise. It starts with trailing dimensions and works ots way forward. Two dimensions are compatible when:
  * they are equal, or
  * one of them is 1
    
```python
a2
# console:
array([[1. , 2. , 3. ],
       [4. , 6.5, 7. ]])

a3
# console:
array([[[ 1,  2,  3],
        [ 4,  5,  6],
        [ 7,  8,  9]],

       [[10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]]])

a2.shape
# console >> (2, 3)

a3.shape
# console >> (2, 3, 3)

a2 * a3
# console >> ValueError: operands could not be broadcast together with shapes (2,3) (2,3,3) 

a2.reshape(2,3,1).shape
# console >> (2, 3, 1)

# Do a reshape:
a2_reshaped = a2.reshape(2,3,1)

# Do multiplication of arrays:
a2_reshaped * a3
# console: 
array([[[  1. ,   2. ,   3. ],
        [  8. ,  10. ,  12. ],
        [ 21. ,  24. ,  27. ]],

       [[ 40. ,  44. ,  48. ],
        [ 84.5,  91. ,  97.5],
        [112. , 119. , 126. ]]])
```
#### Transposing

* Transpose = switches the axis'

```python
a2
# console:
array([[1. , 2. , 3. ],
       [4. , 6.5, 7. ]])

# Transpose array a2:
a2.T
# console:
array([[1. , 4. ],
       [2. , 6.5],
       [3. , 7. ]])

# Show transposed shape:
a2.T.shape
# console >> (3, 2)
```

#### Dot product
* Dot product is just another way of finding patterns between two different sets of numbers
```python
np.random.seed()

mat1 = np.random.randint(10, size=(5, 3))
mat2 = np.random.randint(10, size=(5, 3))


mat1
# console:
array([[0, 1, 0],
       [1, 4, 7],
       [9, 4, 9],
       [2, 6, 2],
       [5, 5, 4]])


mat2
# console:
array([[6, 2, 3],
       [9, 5, 0],
       [6, 1, 1],
       [4, 9, 9],
       [6, 0, 4]])


# Element-wise multiplication
mat1 * mat2
# console:
array([[ 0,  2,  0],
       [ 9, 20,  0],
       [54,  4,  9],
       [ 8, 54, 18],
       [30,  0, 16]])


# Dot product multiplication:
np.dot(mat1, mat2)
# console >> ValueError: shapes (5,3) and (5,3) not aligned: 3 (dim 1) != 5 (dim 0)

# NOTE: It's not working because shapes (5,3) (5,3) are not aligned - meaning Numbers on the inside must match. 
# Meaning we need to have shapes like (5,3) and (3,5)
# NOTE: check http://matrixmultiplication.xyz/
# Solution: use transpose on matrix to solve it


np.dot(mat1,mat2.T)
# console:
array([[  2,   5,   1,   9,   0],
       [ 35,  29,  17, 103,  34],
       [ 89, 101,  67, 153,  90],
       [ 30,  48,  20,  80,  20],
       [ 52,  70,  39, 101,  46]])
```


### Sorting arrays


### Practical use cases

