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

# # Indtoruction to Matplotlib

# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

x = [1,2,3,4]
y = [11,22,3,44]
plt.plot(x, y)

fig, ax = plt.subplots()
ax.plot(x,y)


