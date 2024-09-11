import numpy as np

'''

create numpy array

'''


num_list = list(range(0,50,2))
list_list = [[1,2,3], [4,5,6], [7,8,9]]

my_array = np.array(num_list)
my_array = np.array(list_list)

my_array = np.arange(0,11,2)

my_array = np.zeros((4,5))              ### make array of all zeros with 4 rows and 5 columns

my_array = np.ones((4,5))               ### make array of all ones with 4 rows and 5 columns

my_array = np.linspace(0, 10, 20)       ### 20 evenly spaced points between 0 and 10


my_array = np.eye(10)                    ### square matrix with a diagonal row of 1s


my_array = np.random.rand(5,3)          ### 5 by 3 matrix with random numbers along normal distribution between 0 and 1

my_array = np.random.randn(5,3)         ### 5 by 3 matrix with random numbers along normal distribution focused on 0

my_array = np.random.randint(1, 10, 6)      ### 5 random integers between 1 and 10


num_list = list(range(0,50,2))

my_array = np.array(num_list)

# print("first array \n" , my_array)


new_array = my_array.reshape(5,5)           ### does not mutate original array, but creates a new one

# print("reshaped array \n", new_array)


my_array = np.random.randint(0, 100, 15)

new_array = my_array.reshape(3,5)

max_int = new_array.max()
min_int = new_array.min()

# print(new_array)
# print("max", max_int)
# print("min", min_int)
# print("max position", new_array.argmax())
# print("min position", new_array.argmin())

my_array = np.arange(0, 100, 5)                 ### Create array

# print("original array: \n", my_array)

new_array = my_array.copy()                 ### Copy array
new_array = new_array[0:5]                 ### Slice array

# print("slice\n", new_array)

new_array[:] = 7                 ### Broadcast new integer to the slice

# print("sliced array: \n", new_array)                 ### New integer in slice
# print("original array: \n", my_array)                 ### Does not change original array because we copied it

divide_by_3 = my_array % 3 == 0             ### returns an array of boolean values for each item in the array

# mod_3 = my_array[divide_by_3]           ### returns an array of values from original array where values are true

mod_3 = my_array[my_array % 3 == 0]     ### same as line 76

# print(my_array)
# print(divide_by_3)

my_array = np.arange(64).reshape(8,8)

print(my_array)

print('slice\n', my_array[4:,:7])


small_arr = np.arange(0,11)
large_arr = np.arange(0,20)

# added_array = small_arr + large_arr           ### can't do this because the arrays are not the same shape


err = small_arr / 0         ### does not give an error and still gives feedback

# print(err)

print("\n=========================================\n")

my_array = np.zeros(10)

print("\nzeros array:\n\n", my_array)

my_array = np.ones(10)

print("\nones array:\n\n", my_array)

my_array = np.ones(10) * 5

print("\nfives array:\n\n", my_array)

my_array = np.arange(10,50)

print("\n10 to 50 array:", my_array)

my_array = np.arange(10,50,)
my_array = my_array[my_array % 2 == 0]
# my_array = np.arange(10,51,2)


print("\n10 to 50 array all even:\n\n", my_array)

my_array = np.arange(0,9).reshape(3,3)

print("\n 0 to 8 - 3x3 \n\n", my_array)

my_array = np.eye(3)

print("\n identity matrix 3x3: \n\n", my_array)

my_array = np.random.rand(1)


print("\n random integer: \n\n", my_array)


my_array = np.random.randn(5,5)

print("\n normal dist 25 random: \n\n", my_array)

my_array = np.arange(1,101).reshape(10,10) / 100
""" OR """
# my_array = np.linspace(1,101).reshape(10,10)

print("\n copied matrix: \n\n", my_array)

my_array = np.linspace(0,1,20)

print("\n 20 linear spaced: \n\n", my_array)


mat = np.arange(1,26).reshape(5,5)


my_array = mat.copy()[2:, 1:]


print("\n matrix indices selection: \n\n", my_array)

my_array = mat.copy()[3, -1]

print("\n matrix single selection: \n\n", my_array)
print(mat)

my_array = mat.copy()[:3,1].reshape(1,3)

print("\n matrix selection: \n\n", my_array)

my_array = mat.copy()[-1:,:]

print("\n matrix last row: \n\n", my_array)

my_array = mat.copy()[-2:, :]

print("\n matrix last 2 rows: \n\n", my_array)

print(mat.sum())                    ### get sum of whole matrix
print(mat.std())                    ### get standard deviation of whole matrix
print(mat.sum(0))                   ### get sum of all columns
print(mat.sum(-1))                  ### get sum of each row