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
# console >> (2, 3, 3)

# Show number of dimensions of our arrays:
a1.ndim, a2.ndim, a3.ndim
# console >> (1, 2, 3)

# Show datatypes of our arrays:
a1.dtype, a2.dtype, a3.dtype
# console >> (dtype('int32'), dtype('float64'), dtype('int32'))

# Show number of elements in arrays:
a1.size, a2.size, a3.size
# console >> (3, 6, 18)

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
# console >> array([[1, 1, 1], [1, 1, 1]])

# zeroes() function will return a new array of given shape and type filled with zeros
zeros = np.zeros(shape=(2,3), dtype=float)
zeros
# console >> array([[0., 0., 0.], [0., 0., 0.]])

# arrange() function to create array from range like: start-stop-step
range_array = np.arange(0,10,2)
range_array
# console >> array([0, 2, 4, 6, 8])

# random array using random.randint() function to create integers in range from low to high
random_array = np.random.randint(low=0, high=10, size=(3,5))
random_array
# console >> array([[7, 4, 4, 7, 0], [0, 0, 9, 5, 7], [7, 8, 3, 9, 1]])

# random array using random.random() function to create floats in the half-open interval from 0 to 1
random_array2 = np.random.random((2,3))
random_array2
# console >> array([[0.90025663, 0.22956566, 0.94998119], [0.17103584, 0.86062334, 0.20246913]])

# random array using random.rand() function to create random values in the given shape
random_array3 = np.random.rand(2,3)
random_array3
# console >> array([[0.68284128, 0.48876519, 0.79986118], [0.86774647, 0.13287731, 0.5262673 ]])

# Pseudo-random arrays - allows us to create random arrays that are reproducable 
# line below ensures that our random_array4 will be the same no matter how many times we will run this command :) 
np.random.seed(seed=0)
random_array4 = np.random.randint(10, size=(5,3))
random_array4
```

### Viewing arrays and matrices
Functions to be used:

 * unique() - to find the unique elements of the array
 * 
 * 

### Manipulating and comparing arrays


### Sorting arrays


### Practical use cases

