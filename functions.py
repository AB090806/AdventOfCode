file = (((open("puzzleInput.txt", "r")).read()).strip("\n")).splitlines()
numberWords = ["zero","one","two","three","four","five","six","seven","eight","nine"]


keyNumbers = []


def reverseList(a):
    newList = a[::-1]
    return newList

def numberFromFront(a,b,c):
    # a = keyElement, b = keyDigits, c = keyNumbers
    alreadyFound = []
    for i in range(len(numberWords)):
        word = a.find(numberWords[i])
        if word != -1:
            alreadyFound.append(word)
        foundFront = False
        for j in range(len(b)):
            integer = b[j].isdigit()
            if integer == True and word>j-1 and word > alreadyFound[len(alreadyFound)]:
                c.append(str(b[j]))
                foundFront = True
                break
            elif integer == False and foundFront == False and word > alreadyFound[len(alreadyFound)]:
                c.append(str(i))
                foundFront = True
                break
            else:
                if integer == True and word>j-1:
                    c.append(str(b[j]))
                    foundFront = True
                    break
                elif integer == False and foundFront == False:
                    c.append(str(i))
                    foundFront = True
                    break
        if foundFront == True:
            break




for i in range(len(file)):
    keyElement = file[i]
    keyDigits = []
    for j in range(len(keyElement)):
        keyDigits.append((keyElement[j]))
    numberFromFront(keyElement,keyDigits,keyNumbers)

print(keyNumbers)