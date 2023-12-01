file = (((open('puzzleInput.txt', 'r')).read()).strip('\n')).splitlines()

for i in range(len(file)):
    keyElement = []
    keyNumbers = []
    for k in range(len(file[i])):
        keyElement.append((file[i][k]))
    found1 = False
    for m in range(len(keyElement)):
        while found1 == False:
            if keyElement[m].isnumeric() == True:
                keyNumbers.append(keyNumbers[m])
                found1 = True
    reversed = keyElement.reverse()
    found2 = False
    for n in range(len(reversed)):
        while found2 == False:
            if reversed[n].isnumeric() == True: 
                keyNumbers.append(reversed[n])
                found2 = True

print(reversed)