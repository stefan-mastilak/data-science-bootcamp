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

## Anatomy of plot

<img width="998" alt="matplotlib-anatomy-of-a-plot" src="https://user-images.githubusercontent.com/74961891/174809783-da778aa4-d7c9-447b-9804-d33511506b12.png">

<img width="997" alt="matplotlib-anatomy-of-a-plot-with-code" src="https://user-images.githubusercontent.com/74961891/174809910-8d394f58-042a-4782-8eb1-fed97972b3e6.png">
