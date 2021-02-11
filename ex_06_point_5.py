text = "X-DSPAM-Confidence:    0.8475";
ipos = text.find(":")
piece = text[ipos+5:]
output = float(piece)
print(output) # printing the string after the index position of ipos+5
