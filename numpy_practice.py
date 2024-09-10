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

print(new_array)
print("max", max_int)
print("min", min_int)
print("max index", new_array.argmax())
print("min index", new_array.argmin())


