# To get Method for Dictionaries

# The pattern of checking to see if a key is already
# in a dictionary and assuming a default value if the key
# is not there is so commojn that there is a method called get()
# that does this for us

# Default value if key does not exist (and no Traceback)


if name in counts:
    x = counts[name]
else:
    x = 0

x = counts.get(name, 0)

{'csev' : 2 , 'zqian' : 1 , 'cwen' : 2}