# Numpy for Mathematical Computations
Numpy stands for Numerical Python and it is used for computing mathematical equations and functions. Other mathematical and data science dominant packages rely on Numpy.
The package has to be imported before it can be used.

### Creating Arrays
There are numerous ways to create an array, including:
1. **np.array()**: Takes a list of values
2. **np.zeros(n)**: Fills an array with the specified amount of 0s.
3. **np.ones**()
4. **np.empty(n)**: ones, zeros, and empty can take a tuple to specify the shape, np.empty((2, 3, 4))
5. **np.arange(n)**: similar to the range function, if n is 3 it creates an array with [0, 1, 2]
6. **ones_like/zeros_like()**: creates an array of 1s or 0s based on the shape of a given array.
**identity**: creates an identity matrix: 1s on the diagonal and 0s everywhere else.


### Ways to check data
- np.shape: displays the number or columns and rows, if it's multi-dimensional it displays the dimensions.
- np.ndim: number of dimensions
- np.dtype: datatype

The datatype can be specified during creation:
```py
fun_array = np.array([2, 4, 6], dtype=np.int32)
# Convert with astype()
fun_array = fun_array.astype(np.float)
```

### Arithmetic Operation
For standard operations like add, minus, divide, substract, and multiply, each value will be computed respectfully. 

### Indexing and Slicing
Use slicing: [:]
The reshape() method allows the values to take a specified shape: arr.reshape((rows, columns))
