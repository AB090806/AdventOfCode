file = (((open("puzzleInput.txt", "r")).read()).strip("\n")).splitlines()
numberWords = ["zero","one","two","three","four","five","six","seven","eight","nine"]


keyNumbers = []


def reverseList(a):
    newList = a[::-1]
    return newList

def numberFromFront(a,b,c,d):
    # a = keyElement, b = keyDigits, c = keyNumbers, d = keyPointers
    for i in range(len(a)):
        found = False
        for j in range(len(numberWords)):
            for k in range(len(b)):
                integer = b[k].isdigit()
                pointer = a.find(numberWords[j])
                if integer == True and pointer>k-1:
                    c.append(str(b[k]))
                    found = True
                    break
                elif found == False and pointer != -1 and integer == False:
                    c.append(str(j))
                    found = True
                    break
                



for i in range(len(file)):
    keyElement = file[i]
    print(keyElement)
    keyDigits = []
    keyPointers = []
    for j in range(len(keyElement)):
        keyDigits.append((keyElement[j]))
    numberFromFront(keyElement,keyDigits,keyNumbers,keyPointers)

print(keyNumbers)