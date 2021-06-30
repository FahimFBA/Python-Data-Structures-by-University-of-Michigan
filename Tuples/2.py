# Tuples are "immutable"

# Unlike a list, once you create a tuple, you cannot alter its contents - similar to a string

x = [9, 8, 7]
x[2] = 6
print(x)

# Output: [9, 8, 6]

y = 'ABC'
y[2] = 'D'
print(y)

# Output: TypeError: 'str' object does not support item assignment

z = (5, 4, 3)
z[2] = 0
print(z)

# Output: TypeError: 'str' object does not support item assignment
