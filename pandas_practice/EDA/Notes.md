# Exploratory Data Analysis
EDA is the process of reviewing and cleaning data to gain insights and test hypotheses.
There are a few quick methods to help you understand your dataset:
- __describe()__ : shows a series of summary statistics for numeric data sets;
- __info()__ : displays the data types in columns;
- __head()__ : returns the first few columns and fields of the dataset;
- __tail()__ : returns the last few columns and fields of the dataset.

Data validation is about testing the accuracy of the data in terms of the column values needed. There are a few methods and attributes in pandas to help with this:
- __dtypes__ : States what type of data is stored in a column;
- __astype()__ : Easily converts a data type to another of a specified column;
- __isin()__ : returns True/False for a specified value in a column;
- __select_dtypes()__ : allows for specific columns to be displayed;
- __min()__ and __max()__ : shows the miniumum and maximum values in a column respectively.
```python
cars.dtypes
cars['Cost_USD'].astype(float)
cars['Brand'].isin(['Ford', 'Toyota'])  # ~ reverse True/False
cars.select_dtypes('number')  # returns column with type int and float
cars['Years'].min()
```

Data summarisation allows for statistics to be calculated based on subset values. It uses the **agg()** method to apply different statistical methods to numeric data. Common statistical methods are: *mean*, *count*, *median*, *std*, *min*, *max*, and *var*. The **groupby()** method allows data to be grouped by a certain column, where stats can be placed on them in combination with the agg() method or without.
```python
shops.groupby('item_price').mean()
shops.agg(['median', 'count'])  # applies to numeric columns
# The agg() can use a dict to apply which methods would be 
# ...used on which column
shops.agg({'year': ['mean'], 'cost': ['median', 'std']})

# The agg() and groupby() can combine to create new columns
# ... using tuples
cars.groupby('Brand').agg(
    # must has the column name to run the stat on first
    mean_rating=('ratin', 'mean'),
    std_rating=('rating', 'std')
    median_year=('year', 'median)
)
```

## Data Cleaning
Data cleaning is a fun and vital part of data analysis. It is the process of finding inaccurate, incomplete, and inconsistent data and handling them. This process is needed as it makes the data more reliable to use for analysis.

There are numerous ways to deal with missing values such as removing them or replacing them with some other value. The first step is to check if the dataset contains any missing values using the **isna()** method, which by itself returns a list of columns; however, in combination with sum(), it shows how many missing values are in the dataset per column.
```python
nobel.isna().sum()  # Number of NA values in columns

# Drop the columns that do not meet a 5% threshold
threshold = len(shops) * 0.05  # gives the upper-limit needed
# List of columns to drop
drop_cols = shops.columns[shops.isna().sum() <= threshold]
shops.dropna(subet=drop_cols, inplace=True)  # removes the columns from the dataset

# Fill values that are missing with a median() value
prices_dict = cars.groupby('Brand')['Cost_USD'].median().to_dict()
# Use the map() to input the median for the missing values
cars['Cost_USD'] = cars['Cost_USD'].fillna(cars['Brand'].map(prices_dict))
```

Useful methods to check the number of values and uniques values in a column:
- __nunique()__ : returns the number of unique values;
- __value_counts()__ : return the number of different values in a column. For instance, if a column name is Animal, it can return cats = 114 and dogs = 431.

The **str.contains()** searches for specific values, which can be used to filter a dataset or extract the values:
```python
drinks['Type'].str.contains('Alcohol')  # returns True/False 

# To search for more than one value use a pipe between the values
drinks['Type'].str.contains('Milk|Beer')
# Use the carrat ^ symbol to find values that start with a specific value
drink['Type'].str.contains('^Mix')

# Find multiple phrases
drinks_list = ['Beer', 'Vodka', 'Rum n Coke', 'Magarita', 'Mix n Go']
beer = 'Beer|Brew'
vodka = 'Ice|Vodka'
rum = 'Rum|Mix with Coke'
mag = 'Sunset|Colours'
mix = 'Mix Drinks'  # Conditions to search
conditions = [
    (drinks['Type'].str.contains(beer)),
    (drinks['Type'].str.contains(vodka)),
    (drinks['Type'].str.contains(rum)),
    (drinks['Type'].str.contains(mag)),
    (drinks['Type'].str.contains(mix))
]
# Create the new column
drinks['Drink_Type'] = np.select(conditions, drink_list, default='Water')
```

String values can be converted to numeric values by following two steps:
```python
cars['Price_in_EU'] = cars['Price_in_EU'].str.replace(',', '')
cars['Price_in_EU'] = cars['Price_in_EU'].astype(float)
```

A new column can be created directly using summary statistics in pandas:
- Use the groupby() method;
- Select the column that the stat will be used on;
- Use the transform method;
- Use a lambda function in the transform method
```python
wages['mean'] = wages.groupby('Experience')['Salary_USD'].tranform(lambda x: x.mean())
```

Outliers are numeric values that are outside those calculated in percentiles. That is, they are some stretch away from the minimum and maximum calculated values. To check for outliers, you'll need to know the 75th and 25th percentile:
```python
seventy_fifth = wages['Salary_USD'].quantile(0.75)
twenty_fifth = wages['Salary_USD'].quantile(0.25)
iqr = seventy_fifth - twenty_fifth
# Outliers outside the ranges
lower_bound = twenty_fifth - (iqr * 1.5)
upper_bound = seventy_fifth + (iqr * 1.5)
wages[wages['Salary_USD'] < lower_bound | shops['Salary_USD'] > upper_bound] \
    [['Experience', 'Location', 'Salary_USD']]
```

## Relationships in Data
Some columns in a dataset relate to eachother. For instance, a dataset about a football/soccer club with columns for dates and upgrade_time may relate. That is, one will show the date in a string format, while the other may show the number of years before an update. The datetime column can be changed from string object to a datetime object:
```python
football_read = pd.read_csv('../football_data.csv', parse_dates=['date'])
football.dtypes
```
The date column can also be updated after the data frame is created using **pd.to_datetime()**. Additionally, if column were in the form of year, month, and day; The method can be used to create one column using thos values:
```python
football['date_time'] = pd.to_datetime(football['month', 'day', 'year'])
```
The attributes **dt.month, dt.day, and dt.year** can be used to extract the specific part of a date.
```python
football['match_month'] = football['date_time'].dt.month
```
Line plots are great to show the relationship between columns:
```python
sns.lineplot(data=football, x='match_month', y='upgrade_time')
```

Correlation describes the strenght and direction between two variables, which helps with predicting outcomes. The **corr()** method is used to show this in datasets.
- Negative : as one variable increases, another decreases;
- Value close to 0 : shows a weak relationship;
- Value close to 1/-1: shows stronger relationships.
The method calculates the Pearson correlation, measuring the linear relationship. The heatmap() graph is colour-coded, where lighter colours are closer to the negative:
```python
sns.heatmap(football.corr(), annot=True)
```
The **pairplot()** graph aggregates several scatterplots into one visual:
```python
sns.pairplot(data=football, vars=['year', 'trophies'])
```
The Kernel Deensity Estimate (KDE) plots allows visualisation of categorical data, showing their relationships.
```python
sns.kdeplot(data=football, x='update_time', hue='trophies', cut=0, cumulative=True)  # The cut argument states where to cut off the graph plots
```

## Useful Techniques
The **normalize** argument in the value_counts() method shows the relative frequenccy of values. Cross_tabulation can show how observations occur in combination.
```python
print(salaries['Wages'].value_counts(normalize=True))
print(pd.crosstab(salaries["Company_Size"], salaries["Experience"]))

# Calculate the mean 
print(pd.crosstab(
    salaries['Job_Category'], salaries['Company_Size'],
    values=salaries['Salary_USD'], aggfunc='mean'
))
```
The **dt.weekday** attribute uses numbers to show the date where Monday is represented as 0.

New features can be created using the **pd.cut** method:
```python
salary_labels = ['entry', 'mid', 'senior', 'exec']
# Create the salary ranges list
salary_ranges = [0, twenty_fifth, salaries_median, seventy_fifth, salaries["Salary_USD"].max()]
salaries['salary_level'] = pd.cut(salaries['Salary_USD'], bins=salary_ranges, labels=salary_labels)
```