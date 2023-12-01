file = (((open('puzzleInput.txt', 'r')).read()).strip('\n')).splitlines()
total = 0

for i in range(len(file)):
    x = 0
    for j in range(len(file[i])):
        if file[i][j].isnumeric() == True:
            x = int(file[i][j]) + x
    total = total + x

print(total)