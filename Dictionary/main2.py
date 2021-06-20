# When we see a new name

# When we encounter a new name, we need to add a new entry in the dictionary
# and if this the second or later time we have seen the name,
# we simply add one to the count in the dictionary under that name

counts = dict()
names = ['csev' , 'cwen' , 'csev' , 'zaian' , 'cwen']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# Output: {'csev': 2, 'cwen': 2, 'zaian': 1}
