'''

Present a dataset and a function

'''

num = range(5,10)

def square(number):
    return number * number


'''

combine both

'''


old_value = []

for n in num:
    x = square(n)
    old_value.append(x)


print("Original value is: \n", old_value)


'''

Simple method is this ...

'''


new_value = list(map(square, num))

print("Simple value is: \n ", new_value)


'''

Keep in mind:
-- Tuple Unpacking
-- methods
-- lamba functions


'''