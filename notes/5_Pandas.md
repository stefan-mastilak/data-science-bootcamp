----------------------------------------
Machine learning & Data science Bootcamp
----------------------------------------

## Pandas
   * data analysis tool in python 
   * it's simple to use and integrated with many other data science and ML Python tools
   * it helps you get your data ready for a machine learning
   * everything will be explained in the notebooks/pandas_introduction.ipynb 

<img width="993" alt="pandas-anatomy-of-a-dataframe" src="https://user-images.githubusercontent.com/74961891/168790140-a9c7f07b-412b-4fcc-8dc5-f84d83701822.png">

### Main data types in Pandas:

   * Series
      * one-dimensional

   * DataFrame
      * two-dimensional
     
```python
  # Series: 1-dimenional data
  series = pd.Series(["BMW", "Toyota", "Honda"])
  colours = pd.Series(["Red", "Blue", "White"])
  # DataFrame: 2-dimenional data
  car_data = pd.DataFrame({ "Car make": series, "Colour": colours })
```
    
### Importing and exporting data

```python
  # import data an export to csv:
  car_sales = pd.read_csv("car-sales.csv")
  car_sales.to_csv("exported-car-sales.csv", index=False)
  export_car_sales = pd.read_csv("exported-car-sales.csv")
  
  # Import data and export to excel:
  car_sales = pd.read_csv("car-sales.csv")
  car_sales.to_excel("exported-car-sales.xlsx", index=False)
  export_car_sales = pd.read_excel("exported-car-sales.xlsx")
  
  # Data imported from URL:
  heart_disease = pd.read_csv("data/heart-disease.csv")
  heart_disease = pd.read_csv("https://raw.githubusercontent.com/data/heart-disease.csv")
```

### Describe data

   * dtypes - attribute that shows data types of the dataframe objects
   * columns - attribute that shows dataframe columns
   * index - attribute that shows range of indexes in your dataframe
   * describe() - function that gives some statistic info about our data (it works only on numeric columns)
   * info() - function that shows information about the dataframe
   * mean() - function that do sum of a column values
   * len() - function that returns length of dataframe
     
```python
# Attribute - information
car_sales.dtypes

# Function - contain code to execute
# car_sales.to_csv()

car_sales_columns = car_sales.columns # get all columns
car_sales_index = car_sales.index # get index column
car_sales.describe() # get count, mean, std, min, max, percentile
car_sales.info() # get details of car_sales
car_sales.mean()
car_prices = pd.Series([3000, 1500, 111250])
car_prices.mean()
car_sales.sum()
car_sales["Doors"].sum()
len(car_sales)
```

### Selecting and viewing data
   
   * head() - show first rows of your dataframe (5 by default)
   * tail() - show last rows of your dataframe (5 by default)
   * loc() - refers to index - it shows what is on the index
   * iloc() - refers to position - it shows what is on the position
   * car_sales[car_sales["Make"] == "Toyota"] - filter on data where Make equals 'Toyota'
   * car_sales[car_sales["Odometer (KM)"] > 80000] - filter on data where Odometer has more than 80000 km

```python
car_sales.head() # get top 5 rows of car_sales
car_sales.head(7) # get top 7 rows of car_sales
car_sales.tail() # get bottom 5 rows of car_sales

# index [0, 3, 9, 8, 3] => ["cat", "dog", "bird", "panda", "snake"]
animals = pd.Series(["cat", "dog", "bird", "panda", "snake"], index=[0, 3, 9, 8, 3])
animals.loc[3]  # loc refers to index
animals.iloc[3] # iloc refers to position
car_sales.loc[3]  # car_sales item has same position and index
car_sales.iloc[3]

animals.iloc[:3]  # 1st to 3rd positions, 4th is excluded
car_sales.loc[:3] # index 0 to 3 (included)

car_sales["Make"] # get column Make method 1 - column name can be more than 2 words with space
car_sales.Make  # get column Make method 2 - column name must be 1 word without space

car_sales[car_sales["Make"] == "Toyota"] # select rows with criteria - ["Make"] == "Toyota"
car_sales[car_sales["Odometer (KM)"] > 100000] # select rows with criteria - ["Odometer (KM)"] > 100000
pd.crosstab(car_sales["Make"], car_sales["Doors"]) # show the relationshop of "Make" and "Doors"
car_sales.groupby(["Make", "Colour"]).mean() # group row by "Make", then "Colour"

car_sales["Odometer (KM)"].plot() # plot a line graph
car_sales["Odometer (KM)"].hist() # plot a histogram
car_sales["Price"].dtype # check data type of "Price" column
# convert "Price" column value to integer type
car_sales["Price"] = car_sales["Price"].str.replace('[\$\,\.]','').astype(int)
```

### Comparing data

   * crosstab() - function to compare two columns 
   * groupby() - function to compare more than two columns

### Plotting data
   
   * plotting works only for numerical data
   * plot() - visualising function
   * hist() - histogram function

### Manipulating data

   * str.lower() - function for lowering characters
   * str.upper() - function for uppering characters

### Missing data

   * problem that usually occurs in real project
   * fillna() - function to fill missing values - use fillna() function where you can use mean value calculated from the existing values
   * dropna() - function for dropping all rows that have some unfilled values within

### Creating columns

   * columns from series
   * columns from python list - list length must be the same as length of df
   * column created from another column by calculation
   * column created from a single value

### Deleting columns 

   * drop() - function for deleting column in dataframe 

### Randomizing order

   * sample(frac=0.5) - function for shuffling data, frac parameter defines fraction of data (0-1)
   * reset_index() - reset shuffled data and order them based on their index

### Applying functions

   * lambda functions could be called within dataframe
   * car_sales["Odometer (KM)"] = car_sales["Odometer (KM)"].apply(lambda x: x/1.6)

```python
car_sales["Make"].str.lower()
car_sales["Make"] = car_sales["Make"].str.lower()

car_sales_missing = pd.read_csv("car-sales-missing-data.csv")
odometer-mean = car_sales_missing["Odometer"].mean() # get the mean value of Odometer column

car_sales_missing["Odometer"].fillna(odometer-mean) #   replace NaN with mean value
# update car_sales_missing method 1 - inplace=True
car_sales_missing["Odometer"].fillna(odometer-mean, inplace=True)
# update car_sales_missing method 2 - assign new values to car_sales_missing["Odometer"]
car_sales_missing["Odometer"] = car_sales_missing["Odometer"].fillna(car_sales_missing["Odometer"].mean())

car_sales_missing.dropna(inplace=True)
car_sales_missing_dropped = car_sales_missing.dropna()
car_sales_missing_dropped.to_csv("car-sales-missing-dropped.csv")

# Create a column from series
seats_column = pd.Series([5, 5, 5, 5, 5])
car_sales["Seats"] = seats_column
car_sales["Seats"].fillna(5, inplace=True)

# Create a column from Python list
# list must have same length as exsiting data frame
fuel_economy = [7.5, 9.2, 5.0, 9.6, 8.7, 4.7, 7.6, 8.7, 3.0, 4.5]
car_sales["Fuel per 100KM"] = fuel_economy

# Derived a column
car_sales["Total fuel used (L)"] = car_sales["Odometer (KM)"] / 100 * car_sales["Fuel per 100KM"]
car_sales["Total fuel used"] = car_sales["Odometer (KM)"] / 100 * car_sales["Fuel per 100KM"]

# Create a column from a single value
car_sales["Number of wheels"] = 4
car_sales["Passed road safety"] = True

# Delete a column
# axis=1 - refer to column
car_sales.drop("Total fuel used", axis=1, inplace=True)

# get a sample data set - 20% of data
car_sales_shuffled = car_sales.sample(frac=0.2)

# reset index column to original value
car_sales_shuffled.reset_index(drop=True, inplace=True)

# apply lambda function to Odometer (KM) column
car_sales["Odometer (KM)"] = car_sales["Odometer (KM)"].apply(lambda x: x / 1.6)
```