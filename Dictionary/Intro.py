# Lists index their entries based on the position in the list

# Dictionaries are like bages - no order

# So we index the things we put in the dictionary with a "lookup tag"

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)

print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse)