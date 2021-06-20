# Dictionary Tracebacks

# It is an error to reference a key which is not in the dictionary

# We can use the in operator to see if a key is in the dictionary

ccc = dict()
print(ccc['csev'])

# Output:
#
# Traceback (most recent call last):
#   File "C:\Users\FBA_Desktop\PycharmProjects\PythonCodes\main1.py", line 8, in <module>
#     print(ccc['csev'])
# KeyError: 'csev'



print('csev' in ccc) # Output: False