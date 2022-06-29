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
    * Split your data first (into train/test), always keep your training & test data separate
    

* Filling (imputing) or disregarding missing values
    * Fill/transform the training set and test sets separately 
    * this goes for filling data with pandas as well
    * Don't use data from the future (test set) to fill data from the past (training set)
    

* Converting non-numerical values to numerical values (Feature encoding)

#### 1.1) Imports:
```python
# Imports:
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

# Import car sales missing data:
car_sales_missing = pd.read_csv('data/car-sales-extended-missing-data.csv')
car_sales_missing.head(8)
```

#### 1.2) Missing data:
```python
### What if there are missing values?
    # 1. Fill them with some value (also known as imputation)
    # 2. Remove the samples with missing data altogether
    
# Get the sum of the missing columns in the data:
car_sales_missing.isna().sum()

Make             49
Colour           50
Odometer (KM)    50
Doors            50
Price            50
dtype: int64

# Drop the rows with no labels (our case - those with no Price label)
# NOTE: those data are irrelevant, because label is missing here

car_sales_missing.dropna(subset=["Price"], inplace=True)
car_sales_missing.isna().sum()

Make             47
Colour           46
Odometer (KM)    48
Doors            47
Price             0
dtype: int64

# Note: 50 rows will be missing - so 950 rows remained in dataset:
len(car_sales_missing)

950
```

#### 1.3) Data split:
```python
# Split data into x (features matrix) and y (labels matrix):
x = car_sales_missing.drop('Price', axis=1)
y = car_sales_missing['Price']

# Split the data into training and test sets:
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# check the split dataset shapes:
x_train.shape, x_test.shape, y_train.shape, y_test.shape
```

#### 1.4) Missing data filling
  * #### Option 1 - Filling missing data and transforming categorical data with Pandas:

```python
# fill up the make column
car_sales_missing['Make'].fillna('missing', inplace=True)

# fill up the colour column:
car_sales_missing['Colour'].fillna('missing', inplace=True)

# fill up the odometer column:
car_sales_missing['Odometer (KM)'].fillna(car_sales_missing['Odometer (KM)'].mean(), inplace=True)

# fill up the doors column:
car_sales_missing['Doors'].fillna(4, inplace=True)

# check missing data again:
car_sales_missing.isna().sum()

Make              0
Colour            0
Odometer (KM)     0
Doors             0
Price             0
dtype: int64


# Convert data into the numbers:

# Let's try and convert our data to numbers - Turn the categories into numbers:
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

categorical_features = ["Make", "Colour", "Doors"]
one_hot = OneHotEncoder()
transformer = ColumnTransformer([("one_hot",
                                   one_hot,
                                   categorical_features)],
                                   remainder="passthrough")

transformed_X = transformer.fit_transform(car_sales_missing)
```

  * #### Option 2 - Filling missing data and transforming categorical data with Scikit-learn:
    The main takeaways:
    * Split your data first (into train/test)
    * Fill/transform the training set and test sets separately
    * NOTE: It's best to fill and transform training and test sets separately
  
```python
# Check missing values
x.isna().sum()

Make             47
Colour           46
Odometer (KM)    48
Doors            47
dtype: int64

# Fill missing values with Scikit-Learn
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer

# Fill categorical values with 'missing' & numerical values with mean
cat_imputer = SimpleImputer(strategy="constant", fill_value="missing")
door_imputer = SimpleImputer(strategy="constant", fill_value=4)
num_imputer = SimpleImputer(strategy="mean")

# Define columns:
cat_features = ["Make", "Colour"]
door_feature = ["Doors"]
num_features = ["Odometer (KM)"]

# Create an imputer (something that fills missing data):
imputer = ColumnTransformer([
    ("cat_imputer", cat_imputer, cat_features),
    ("door_imputer", door_imputer, door_feature),
    ("num_imputer", num_imputer, num_features)
])

# Fill train and test values separately:
filled_x_train = imputer.fit_transform(x_train)
filled_x_test = imputer.transform(x_test)

# Check filled x_train (note that missing data has been filled):
filled_x_train

array([['Honda', 'White', 4.0, 71934.0],
       ['Toyota', 'Red', 4.0, 162665.0],
       ['Honda', 'White', 4.0, 42844.0],
       ...,
       ['Toyota', 'White', 4.0, 196225.0],
       ['Honda', 'Blue', 4.0, 133117.0],
       ['Honda', 'missing', 4.0, 150582.0]], dtype=object)

# Get our transformed data array's back into DataFrame's
car_sales_filled_train = pd.DataFrame(filled_x_train, 
                                      columns=["Make", "Colour", "Doors", "Odometer (KM)"])

car_sales_filled_test = pd.DataFrame(filled_x_test, 
                                     columns=["Make", "Colour", "Doors", "Odometer (KM)"])

# Check missing data in training set
car_sales_filled_train.isna().sum()

Make             0
Colour           0
Doors            0
Odometer (KM)    0
dtype: int64

# Check to see the original - still missing values here which is exactly what we wanted
car_sales_missing.isna().sum()

Make             47
Colour           46
Odometer (KM)    48
Doors            47
Price             0
dtype: int64


# Convert data into the numbers:
# Now let's one hot encode the features with the same code as before 
categorical_features = ["Make", "Colour", "Doors"]
one_hot = OneHotEncoder()
transformer = ColumnTransformer([("one_hot", 
                                 one_hot, 
                                 categorical_features)],
                                 remainder="passthrough")

# Fill train and test values separately
transformed_x_train = transformer.fit_transform(car_sales_filled_train)
transformed_x_test = transformer.transform(car_sales_filled_test)

# Check transformed and filled X_train
transformed_x_train.toarray()

# Now we've transformed x, let's see if we can fit a model
np.random.seed(42)
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()

# Make sure to use transformed (filled and one-hot encoded x data)
model.fit(transformed_x_train, y_train)
model.score(transformed_x_test, y_test)
```

