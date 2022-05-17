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
      * series = pd.Series(["BMW", "Toyota", "Honda"])
      * colours = pd.Series(["Blue", "Red", "White"])
      

   * DataFrame
      * two-dimensional
      * car_data = pd.DataFrame({"Car make": series, "Colour": colours})
   
    
### Importing and exporting data

   * Importing: car_sales = pd.read_csv("path\to\file")
   * Exporting: car_sales.to_csv("data/exported-car-sales.csv"
   * Importing from URL: car_sales = pd.read_csv("https://raw.githubusercontent.com/myfile.csv")

### Describe data

   * dtypes - attribute that shows data types of the dataframe objects
   * columns - attribute that shows dataframe columns
   * index - attribute that shows range of indexes in your dataframe
   * describe() - function that gives some statistic info about our data (it works only on numeric columns)
   * info() - function that shows information about the dataframe
   * mean() - function that do sum of a column values
   * len() - function that returns length of dataframe

### Viewing data
   
   * head() - show first rows of your dataframe (5 by default)
   * tail() - show last rows of your dataframe (5 by default)
   * loc() - refers to index - it shows what is on the index
   * iloc() - refers to position - it shows what is on the position

### Selecting data

   * car_sales[car_sales["Make"] == "Toyota"] - filter on data where Make equals 'Toyota'
   * car_sales[car_sales["Odometer (KM)"] > 80000] - filter on data where Odometer has more than 80000 km

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