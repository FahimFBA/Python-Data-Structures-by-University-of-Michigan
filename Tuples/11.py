# Even Shorter Version


c = {'a' : 10, 'b' : 1, 'c' : 22}
print(sorted([(v,k) for k,v in c.items()]))

# List comprehension creates a dynamic list.

# In this case, we make a list of reveresd tuples and then sort it

