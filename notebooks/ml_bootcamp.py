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

# ## Heart disease project

# This project is about classifying whether or not a patient has heart disease

import numpy as np
import pandas as pd
import matplotlib
import sklearn

# import data from csv file:

df = pd.read_csv("datasets/heart-disease.csv")

df.head(10)

df.target.value_counts().plot(kind="bar")
