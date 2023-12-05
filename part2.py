file = (((open("puzzleInput.txt", "r")).read()).strip("\n")).splitlines()
numberWords = ["zero","one","two","three","four","five","six","seven","eight","nine"]

keyNumbers = []


def reverseList(a):
    newList = a[::-1]
    return newList

def numberFromFront(a,b,c):
    # a = keyElement, b = keyDigits, c = keyNumbers
    positions = []
    numbers = []

    for i in range(len(a)):
        for j in range(len(numberWords)):
            extract = a[i:i+5]
            if extract.find(numberWords[j]) != -1:
                numbers.append(j)
                positions.append(a.find(numberWords[j]))
                break
    
    if len(positions) != 0:
        firstDigit = positions[0]
    else:
        firstDigit = 100

    for i in range(len(b)):
        integer = b[i].isdigit()
        if integer and i<firstDigit: #could be positions[0]-1
            c.append(str(b[i]))
            break
        elif not integer and i == len(b)-1:
            c.append(str(numbers[0]))
            break
        else:
            True


def numberFromBack(a,b,c):
    # a = keyElement, b = keyDigits, c = keyNumbers
    positions = []
    numbers = []

    for i in range(len(a)):
        for j in range(len(numberWords)):
            extract = a[i:i+5]
            if extract.find(numberWords[j]) != -1:
                numbers.append(j)
                positions.append(a.find(numberWords[j]))
                break
    if len(positions) != 0:
        lastDigit = positions[-1]
    else:
        lastDigit = -100
    for i in range(len(b)-1,-1,-1):
        integer = b[i].isdigit()
        if integer and i>lastDigit:
            c.append(str(b[i]))
            break
        elif not integer and i == -1:
            c.append(numbers[-1])
            break
        else:
            True

for i in range(len(file)):
    keyElement = file[i]
    keyDigits = []
    for j in range(len(keyElement)):
        keyDigits.append((keyElement[j]))
    numberFromFront(keyElement,keyDigits,keyNumbers)
    numberFromBack(keyElement,keyDigits,keyNumbers)

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