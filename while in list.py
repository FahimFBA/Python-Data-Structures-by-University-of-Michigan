numlist = list()
while True:
    inp = input('Enter a number (Enter "stop" to stop the task): ')
    if inp == 'stop':
        break
    value = float(inp)
    numlist.append(value)
average = sum(numlist) / len(numlist)
print('The average is:' , average)