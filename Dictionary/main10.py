# python words.py
# Enter file: words.txt
# to 16



name = input('Enter file: ')
handle = open(name)

counts = dict()


counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1