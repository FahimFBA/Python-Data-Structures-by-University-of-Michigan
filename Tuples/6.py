# Tuples are comparable

# The comparison operators work with tuples and other sequences.
# If the first item is equal, python goes on to the next element, and so on, until it finds elements that differ

print((0,1,2) < (5,1,2))

# True

print((0,1,20000000000) < (0,3,4))

# True

print(('Jones' , 'Sally') < ('Jones' , 'Sam'))

# True

print(('Jones' , 'Sally') > ('Adams' , 'Sam'))

# True