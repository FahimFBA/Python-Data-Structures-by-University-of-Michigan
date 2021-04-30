total = 0
count = 0
while True:
    inp = input('Enter a number (enter "done" to end your tasks): ')
    if inp == 'done':
        break
    value = float(inp)
    total = total + value
    count = count + 1

average = total / count
print('The average is:' , average)