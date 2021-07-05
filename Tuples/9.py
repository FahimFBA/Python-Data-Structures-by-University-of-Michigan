# Sort by values instead of Key

# If we could construct a list of tuples of the form (value, key) we could sort by value

# We do this with a for loop that creates a list of tuples

c = {'a' : 10, 'b' : 1, 'c' : 22}

tmp = list()

for k , v in c.items():
    tmp.append((v,k))
print(tmp)


# Output: [(10, 'a'), (1, 'b'), (22, 'c')]

tmp = sorted(tmp, reverse=True)
print(tmp)


# Output:

# [(10, 'a'), (1, 'b'), (22, 'c')]
# [(22, 'c'), (10, 'a'), (1, 'b')]