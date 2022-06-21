----------------------------------------
Machine learning & Data science Bootcamp
----------------------------------------

## Matplotlib (data visualisation)

* What is Matplotlib
    * Python ploting library
    * Turn date into visualisation
    

* Why Matplotlib?
    * Built on NumPy arrays (and Python)
    * Integrates directly with pandas
    * Can create basic or advanced plots
    * Simple to use interface (once you get the foundations)

```python
# imports:
%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
```
```python
x = [1,2,3,4]
y = [11,22,33,44]

# plot example:
plt.plot(x, y)

# plot example:
fig, ax = plt.subplots()
ax.plot(x,y)
```

## Anatomy of a matplotlib plot

