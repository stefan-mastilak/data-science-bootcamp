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

# ### Plot example workflow

# +
# Imports:

# %matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# +
# Prepare some data:

x = [1,2,3,4]
y = [11,22,3,44]

# Simple plot:
plt.plot(x, y)

# +
# Prepare plot (recommended way):

fig, ax = plt.subplots(figsize=(6,6))
ax.plot(x,y)
# -

type(fig), type(ax)

# +
# Customize plot:

ax.set(title="Simple plot", xlabel="X", ylabel="Y")

# +
# Save and show:

fig.savefig("images/simple_plot.png")
# -


