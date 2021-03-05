# We can look for a string anywhere in a line as our selection criteria

fhand = open('a.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
    print (line)