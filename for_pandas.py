"""

Introduction to Pandas

"""

import numpy as np
import pandas as pd

labels = ['a','b','c']
my_data = [10,20,30]
arr = np.array(my_data)
d = {'a':10,'b':20,'c':30 }

ser = pd.Series(data = my_data)

print(ser)


ser = pd.Series(my_data, labels)

print("\ncreate Series using a list for data and labels:\n", ser)

ser = pd.Series(arr, labels)


print("\ncreate Series using an array and list of labels:\n", ser)


ser = pd.Series(d)


print("\ncreate Series using a dictionary with labels as keys:\n", ser)


########## Panda Series can hold more data types than a NumPy array ##############


ser1 = pd.Series([1,2,3,4], ['USA', 'Germany', 'Bosnia', 'Philippines'])
ser2 = pd.Series([4,5,1,9], ['Cuba', 'USA', 'Portugal', 'Brazil'])

print(ser1)
print(ser2)

print(ser1['USA'])

ser_add = ser1+ser2

print(ser_add)