# Many Counters with a Dictionary

# One common use of dictionaries is counting how often we "see" something

ccc = dict()
ccc['ccev'] = 1
ccc['cwen'] = 1
print(ccc)

# Output: {'ccev': 1, 'cwen': 1}

ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

# Output : {'ccev': 1, 'cwen': 2}