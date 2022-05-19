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
```


### Creating arrays

```python
# Create a Pandas DataFrame from 
import pandas as pd
import numpy as np

a2 = np.array([[1,2,3], [4,6.5,7]])
df = pd.DataFrame(a2)
```

### Viewing arrays and matrices


### Manipulating and comparing arrays


### Sorting arrays


### Practical use cases

