# Using sorted()

# We can do this even more directly using the built-in function sorted that takes a sequence as a parameter and returns a sorted sequence


d = {'a' : 10, 'b' : 1, 'c' : 22}
t = sorted(d.items())
print(t)

# Output: [('a', 10), ('b', 1), ('c', 22)]

for k,v in sorted(d.items()):
    print(k, v)

# Output:

# [('a', 10), ('b', 1), ('c', 22)]
# a 10
# b 1
# c 22