----------------------------------------
Machine learning & Data science Bootcamp
----------------------------------------

## Scikit-learn

* python ML library built on Numpy and Matplotlib
* it has many in-built ML models
* it has methods to evaulate your ML models
* it has very well designed API

### Scikit-learn algorithm cheat-sheet:

![sklearn-ml-map](https://user-images.githubusercontent.com/74961891/175296124-1816827f-29cc-46ac-a137-3959ccd466b8.png)

### Scikit-learn workflow:

![sck](https://user-images.githubusercontent.com/74961891/175296432-317e85fc-599c-4776-ae41-006792952da7.png)

### What we're going to cover:

0) End-to-end Scikit-learn workflow
1) Getting data ready
2) Choose the right estimator/algorythm for our problems
3) Fit the model/algoryth and use it to make predictions on our data
4) Evaulating model
5) Improve model
6) Save and load a trained model
7) Putting it all together

## 1) Getting our data ready
Three main things we have to do:
* Split the data into features and labels (X and Y)
* Filling (imputing) or disregarding missing values 
* Converting non-numerical values to numerical values (Feature encoding)

```python
# standard imports:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# load the data from csv:
heart_disease = pd.read_csv('data/heart-disease.csv')
heart_disease.head()

# create x (features matrix)
x = heart_disease.drop('target', axis=1)
x.head()

# create y (labels matrix)
y = heart_disease['target']
y.head()

# split the data into training and test sets:
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# check the split dataset shapes:
x_train.shape, x_test.shape, y_train.shape, y_test.shape
```