file = (((open('puzzleInput.txt', 'r')).read()).strip('\n')).splitlines()
numberWords = ["one","two","three","four","five","six","seven","eight","nine"]

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
        for n in range(len(numberWords)):
            if numberWords[n] in keyElement[m]:
                keyNumbers.append(j+1)
                break
            elif keyElement[m].isdigit() == True:
                keyNumbers.append(keyElement[m])
                found1 = True
                break

    reversed = reverseList(keyElement)

    found2 = False
    for o in range(len(reversed)):
        for p in range(len(numberWords)):
            if reversed[o].isdigit() == True:
                keyNumbers.append(reversed[o])
                found2 = True
                break
            elif numberWords[p] in keyElement:
                keyNumbers.append(p+1)
                break

print(keyNumbers)

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