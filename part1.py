file = (((open('puzzleInput.txt', 'r')).read()).strip('\n')).splitlines()

def reverseList(a):
    newList = a[::-1]
    return newList

keyNumbers = []

for i in range(len(file)):
    keyElement = []
    for k in range(len(file[i])):
        keyElement.append((file[i][k]))

    found1 = False
    for m in range(len(keyElement)):
        if keyElement[m].isdigit() == True:
            keyNumbers.append(keyElement[m])
            found1 = True
            break

    reversed = reverseList(keyElement)

    found2 = False
    for n in range(len(reversed)):
        if reversed[n].isdigit() == True:
            keyNumbers.append(reversed[n])
            found2 = True
            break

keyConcatenatedNumbers = []
for i in range(0,(len(keyNumbers)-1),2):
    keyConcatenatedNumbers.append((keyNumbers[i]+keyNumbers[i+1]))

keyConcatenatedIntegers = []
for i in range(len(keyConcatenatedNumbers)):
    keyConcatenatedIntegers.append(int(keyConcatenatedNumbers[i]))

totalScore = 0
for i in range(len(keyConcatenatedIntegers)):
    totalScore += keyConcatenatedIntegers[i]

print(totalScore)