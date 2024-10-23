# Exploratory Data Analysis
EDA is the process of reviewing and cleaning data to gain insights and test hypotheses.
There are a few quick methods to help you understand your dataset:
- __describe()__ : shows a series of summary statistics for numeric data sets;
- __info()__ : displays the data types in columns;
- __head()__ : returns the first few columns and fields of the dataset;
- __tail()__ : returns the last few column and fields of the dataset.

Data validation is about testing the accuracy of the data in terms of the column values needed. There are quick a few methods and attributes in pandas to help with this:
- __dtypes__ : States what type of data is stored in a column;
- __astype()__ : Easily converts a data type to another of a specified column;
- __isin()__ : returns True/False for a specified value in a column;
- __select_dtypes()__ : allows for specific columns to be displayed;
- __min()__ and __max()__ : shows the miniumum and maximum values in a column respectively.
```python
cars.dtypes
cars['Cost_USD'].astype(float)
cars['Brand'].isin(['Ford', 'Toyota'])  # ~ reverse True/False
cars.select_dtypes('number')
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