file = (((open("puzzleInput.txt", "r")).read()).strip("\n")).splitlines()
numberWords = ["zero","one","two","three","four","five","six","seven","eight","nine"]

def reverseList(a):
    newList = a[::-1]
    return newList

keyNumbers = []

for i in range(len(file)):
    keyElement = file[i]
    print(keyElement)
    keyDigits = []
    for j in range(len(keyElement)):
        keyDigits.append((keyElement[j]))
    for k in range(len(numberWords)):
        first = keyElement.find(numberWords[k])
        found1 = False
        for m in range(len(keyDigits)):
            digit = keyDigits[m].isdigit()
            if digit == True and m<first:
                keyNumbers.append(str(keyDigits[m]))
                found1 = True
                break
            elif first != -1 and digit == False :
                keyNumbers.append(str(k))
                found1 = True
                break
        if found1 == True:
            break
    reversed = reverseList(keyDigits)
    for n in range(len(numberWords)):
        keyElement = keyElement[::-1]
        second = keyElement.find(numberWords[n])
        found2 = False
        for o in range(len(reversed)):
            digit = reversed[o].isdigit()
            if digit == True and o>second:
                keyNumbers.append(str(reversed[o]))
                found2 = True
                break
            elif second != -1 and digit == False:
                keyNumbers.append(str(n))
                found2 = True
                break
        if found2 == True:
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