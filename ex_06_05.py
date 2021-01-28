str = 'X-DSPAM-Confidence: 0.8475' # a random string

ipos = str.find(':') #find where ':' is located
print(ipos) # printing the value of ipos: location of the ':'
piece = str[ipos+1:]
print(piece) # printing the string after the index position of ipos+1
# print(piece+42.0) # will fail
value = float(piece)
print(value) # printing the float value
print(value+42.0) # printing the float value with addition of 45.0
piece = str[ipos+2:]
print(piece) # printing the string after the index position of ipos+2