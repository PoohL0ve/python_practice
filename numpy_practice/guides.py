""" Learning to Work with Numpy
    Contains different methods and attributes
"""
import numpy as np

# Create Arrays
print('Array Creation')
data: list = [4, 8, 29, 56, 77]
data_array = np.array(data)

two_dim_array = np.array([[2, 5], [3, 4]])
print(f'Two Dimensional Array:\n{two_dim_array}\n')

values: list = [9, 0, 6, 2, 23]
values_array = np.array(values)

zero_values = np.zeros((3, 4), dtype=int)  # Specify data type, default is float
print(f'A 3 by 4 integer array of zeros:\n{zero_values}')
print('****************************')

# Arithmetic
add_both = data_array + values_array
mul_both = data_array * values_array
squared_arr = data_array ** 2

# Indexing and Slicing
arr_range = np.arange(10)
three_five = arr_range[3:5]  # returns the 3rd and 4th value
arr_range[3:5] = 11  # place 11 in both places

two_dim_arr = np.array([[2, 6, 8], [3, 12, 15], [4, 20, 24]])
slice_both = two_dim_arr[:2, 1:]  # [[6, 8], [12, 15]]
print(arr_range)
print(three_five)
print(slice_both)