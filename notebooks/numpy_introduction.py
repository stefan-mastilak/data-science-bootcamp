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

# ### Datatypes and attributes
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

# +
# Create a Pandas DataFrame from 
import pandas as pd

df = pd.DataFrame(a2)
df
# -


