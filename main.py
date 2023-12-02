file = (((open('puzzleInput.txt', 'r')).read()).strip('\n')).splitlines()
numberWords = [["z","e","r","o"],["o","n","e"],["t","w","o"],["t","h","r","e","e"],["f","o","u","r"],["f","i","v","e"],["s","i","x"],["s","e","v","e","n"],["e","i","g","h","t"],["n","i","n","e"]]

def reverseList(a):
    newList = a[::-1]
    return newList

keyNumbers = []

for i in range(len(file)):
    keyElement = []
    keyDigits = []
    for j in range(len(file[i])):
        keyElement.append((file[i][j]))
    for k in range(len(numberWords)):
        for l in range(len(numberWords[k])):
            if 
        else:
            for l in range(len(keyElement)):
                if keyElement[l].isdigit() == True:
                    keyNumbers.append(keyElement[l])
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