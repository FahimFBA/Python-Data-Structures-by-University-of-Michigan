fhand = open('Mytext.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '):
        continue
    words = line.split()
    print(words[2])


line = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2021'
words = line.split()
print(words)
