# Importing Data in Python

# Flat Files
Basic text files end with the extension ".txt" and store simple pieces of data. They can be open and read in Python using the open() method:
```python
filename = 'Never Learning'
file = open(filename, more=r)
text = file.read()
file.close()  # always close the method
```
Another way to open a simple file and automatically close it is with the **with** keyword:
```python
filename = 'Still Trying'
with open(filename, 'r') as file:
    print(file.read())

# The readline() reads a single line
```
The "with" keyword is a content manager that allows you to bind the contents of a file to a variable.

Flat files are text files that contain records in the form of a table (rosw and columns). Values are separated by a delimiter like a comma or dash. They are normally imported with pandas or numpy packages. Numpy arrays are the standard for importing numerical data in Python.
```python
import numpy as np
filename = 'numbers.txt'
data = np.loadtxt(filename, delimiter='-', skiprows=1)  #skips the first row (header)

# The dtype= argument allows for other data types like str
# For specific cols:usecols=[]
```
It is important to either skip the first row or specify the **dtype** argument if the header is a string.

For files with different data types use the pandas package to create Series and DataFrames, which makes it easy to perform statistics. DataFrames allow Exploratory Data Analysis, Data Wrangling, Data preprocessing, Building models, visualisations and more.
```python
import pandas as pd
filename = 'music_docs.csv'
df = pd.read_csv(filename)
# Convert to numpy array
data_array = data.to_numpy()

# If reading in data with paths like C:\, use r to read as a string
books_df = pd.read_csv(r'C:\Users\alert\books.csv', sep=',')

# Read a certain amount of rows
actors_df = pd.read_csv('actors.csv', nrows=10, header=None)
```