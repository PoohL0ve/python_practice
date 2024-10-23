"""
    Exploratory Data Analysis
    EDA is the process of cleaning and reviewing data to gain
    insights and generate hypotheses.

    You can use head(), tail(), info(), and describe() to understand the
    dataset.

    Data Validation:
        The dtypes tells what type of data is stored in columns and the astype()
        can easily change the data type:
            cars.dtypes
            cars['year'] = cars['year'].astype(int)
        The isin() method returns True or false for validating
        whether a value/s is in a column
            cars['make'].isin(['Nissan', 'Toyota'])
            ~cars['make'].isin(['Nissan', 'Toyota'])  inverts True/False
        To only view numbers types: cars.select_dtypes('number')
        The min() and max() shows the minimum and maximum values in a column
            cars['years'].min()
        The 25-75 percentile in a boxplot are coloured, while the
        whiskers are the lowest and highest values.
    
    Data Summarisation:
        The groupby() function allows data to be grouped by a certain
        column:
            cars.groupby('make').mean() - gives the mean of numeric values
            in different columns
            Other agg functions: sum(), count(), min(), max(), var(), std()
        The agg() applies aggregating function across the DataFrame
            cars.agg(['mean', 'std'])
            A dict can specify which function to apply to which column
                cars.agg({'year': ['mean'], 'cost': ['median', 'std']})
        Creating named columns by combining groupby() and agg() using tuples
            cars.groupby('type').agg(
            mean_rating=('rating', 'mean'), # must have a columnName first
            std_rating=()'rating','std'),
            median_year=('year', 'median')
            )
"""
import pandas as pd
import math
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

'''
    Data Cleaning and Imputation
        Addressing missing data
            The isna() checks for NA values in a DF
                shops.isna().sum()
                They can be solved in a number of ways like
                finding a threshold and dropping the columns that 
                don't meet it:
                    threshold = len(shops) * 0.05
                    drop_cols = shops.columns[shops.isna().sum() <= threshold]
                    shops.dropna(subset=drop_cols, inplace=True)
                We can also filter by dictionary and then impute:
                    shop_dict = shops.groupby('Experience')['Salary_USD'].median().to_dict()
                    shops['Salary_USD'] = shops['Salary_USD].fillna(shops['Experience].map(shop_dict))
        
        Converting and Analysing Categorical Data
            Preview the data: shops.select_dtypes('object').head()
            Value and count: shop['Items'].nunique(), shop['Items'].value_counts()
            The str.contains() allows us to check for a soecific value
                shops['Items'].str.contains('Bread')
                    To find more values: shops['Items'].str.contains('Cheese|Butter')
                    Find Phases that has a string: str.contains('^Data')
                The np.select takes the list of conditions, columns to search and default= 'Other'
        
        Working with Numeric Data
            Remove commas: shops[Salary_EU].str.replace(',', '')
            Convert to num: shops[Salary_EU].astype(float)
            Update to USD: shops['Salary_in_Rupee'] * 0.12
        Handling Outliers
            Find percentiles: shops['Salary_USD].quantile(0.75)
            IQR: 75Q - 25Q
            Subset them and include other columns:
                shops[shops['Salary_USD] < lower | shops['Salary_USD] > upper] \
                    [['Experience', 'Location', 'Salary_USD]]
            An easy way to see if there may be inaccurate data is to use the
            describe() on the column and see how far max is from the 75th percentile
'''


'''
    conditions = [
    (planes["Duration"].str.contains(short_flights)),
    (planes["Duration"].str.contains(medium_flights)),
    (planes["Duration"].str.contains(long_flights))
]

# Apply the conditions list to the flight_categories
planes["Duration_Category"] = np.select(conditions, 
                                        flight_categories,
                                        default="Extreme duration")

# Plot the counts of each category
sns.countplot(data=planes, x="Duration_Category")
plt.show()
'''
# To apply a new column based on summury stats"
# shops['std_dev'] = salaries.groupby('Experience')['Salary_USD'].transform(lambda x: x.std())
