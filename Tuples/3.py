# Things not to do with Tuples

x = (3, 2, 1)
x.sort()
print(x)


# Output

# Traceback (most recent call last):
#   File "C:\Users\FBA_Desktop\Desktop\GitHub Repositories\Python-Data-Structures-by-University-of-Michigan\Tuples\3.py", line 4, in <module>
#     x.sort()
# AttributeError: 'tuple' object has no attribute 'sort'

x.append(5)
print(x)

# Traceback

x.reverse()

# Traceback