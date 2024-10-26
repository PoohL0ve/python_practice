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

## Other File Types
Pickled files are native to Python and stores all sorts of data types like dictionaries and lists in bytestreams. This means that the files are serialised.
```python
import pickle
with open('fruits.pkl', 'rb') as file:
    data = pickle.load(file)
# 'rb' means read-only and binary
```
Excel files are one of the most popular and they can be read with pandas:
```python
import pandas as pd
file = 'cosmetics.xlsx'
data = pd.ExcelFile(file)
print(data.sheet_names)
df1 = data.parse('perfume')  # sheet name as a string
df2 = data.parse(0)  # sheet index as a float
# names=[] allow you to specify the cols names
```
You can print the files in the shell
```python
import os
wd = os.getcwd()  # obtains the name of the current directory
os.listdir(wd)  # displays the contents
```

SAS stands for Statistical Analysis System and Stata means Statistics + data. SAS is used in business analytics and biostatistics, while stata is used in academic social sciences research. SAS files are used for:
- Advanced analytics;
- Multivariate analysis;
- Business intelligence;
- Data management;
-Predictive analytics;
- Standard for computational analysis.

The SAS files have the extensions **.sas7bdat** or **.sas7bcat**.
```python
import pandas as pd
from sas7bdat import SAS7BDAT
with SAS7BDAT('finances.sas7bdat') as file:
    df_sas = file.to_data_frame()
print(df_sas.head())
```

Stata file have the extension **.dta**:
```python
import pandas as pd
data = pd.read_stata('workings.dta')
```
Hierarchical Data Format version 5 (HDF5) files are the standard for storing large quantities of numerical data. HDF5 can scale up to exabytes.
```python
import h5py
filename = 'stars.hdf5'
data = h5py.File(filename, 'r')
print(type(data))

# Explore the structure
for key in data.key():
    print(key)
```

Matrix Laboratory (MATLAB) is a numerical computing environment, standard in engineering and science. It has the format **.mat**. 
```python
import scipy.io
filename = 'engineering.mat'
mat = scipy.io.loadmat(filename)
```

## Relational Databases
A database consists of tables, where each table represent one order type. Each row should have a primary identifier. The tables are linked through primary keys as foreign keys. Popular Database Management Systems are PostreSQL, MySQL, and SQLite which use the Structured Query Language (SQL).

SQLite is fast and simple to use. SQLALchemy can be used to create a database engine.
```python
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')
table_names = engine.table_names()  # list of tables

# connect to the database
connect = engine.connect()
# Query: get all column in a table
query = connect.execute('SELECT * FROM ORDERS')
# Save the result as a DF uing fetchall()
df = pd.DataFrame(query.fetchall())  # Fetches all rows
df.columns = query.keys()  # Assign the names of the columns
connection.close()  # close the connection
```
The **with** keyword can also be used to automatically close the connection.
```python
with engine.connect() as con:
    query = con.execute('SELECT OrderID, OrderDate, ShipName FROM ORDERS')
    df = pd.DataFrame(query.fetchmany(size=5))  # 5 rows
    df.columns = rs.keys()
```

Pandas allows the table to be queried in one line:
```python
df = pd.read_sql_query('SELECT * FROM Orders WHERE Value >= 150 ORDER BY Date', engine)
# The engine still has to be created and connected
```

Creating a DataFrame by joining two tables with pandas
```python
from sqlalchemy import create_engine
import pandas as pd
engine = create_engine('sqlite:///Northwind.sqlite')
df = pd.read_sql_query('SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerId = Customers.CustomerId', engine)
print(df.head())