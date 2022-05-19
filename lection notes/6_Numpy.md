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
      * 
<img width="1353" alt="numpy-anatomy-of-a-numpy-array" src="https://user-images.githubusercontent.com/74961891/169284767-c43d0c16-f6d2-465a-b1f4-62bd42b7b785.png">
 
### Data types and attributes (ndarray)

   * Numpy's main datatype is ndarray (n-dimensional array)

```python
# Shape (1,3) - 1 row, 3 columns - one dimension array (vector)
a1 = np.array([1,2,3])

# Shape (2,3) - 1 rows, 3 columns - two dimensional array (matrix)
a2 = np.array([[1,2,3], [4,6.5,7]])

# Shape (3,3,2) - 3 rows, 3 columns, 2 layers - three dimensional array (matrix)
a3 = np.array([[[1,2,3], [4,5,6], [7,8,9]], [[10,11,12],[13,14,15],[16,17,18]]])

# Show shape of array:
a3.shape
>> (2, 3, 3)

# Show number of dimensions of our arrays:
a1.ndim, a2.ndim, a3.ndim
>> (1, 2, 3)

# Show datatypes of our arrays:
a1.dtype, a2.dtype, a3.dtype
>> (dtype('int32'), dtype('float64'), dtype('int32'))

# Show number of elements in arrays:
a1.size, a2.size, a3.size
>> (3, 6, 18)
```


### Creating arrays

```python
# Create a Pandas DataFrame from 
import pandas as pd
df = pd.DataFrame(a2)
```

### Viewing arrays and matrices


### Manipulating and comparing arrays


### Sorting arrays


### Practical use cases

