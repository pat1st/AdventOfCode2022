file1 = open('Day_05\inputTest.txt', 'r')
fileFull = file1.read()

situation, actions = fileFull.split('\n\n')
print(situation)
# print(actions)
situation = situation.split('\n')
newSituation = []

for line in situation:
    newLine = ''
    for char in range(-1, len(line), 2):
        if char>=0:
            newLine += line[char]

    print(newLine)
    newSituation.append(newLine)

print(newSituation)

# for line in range(len(newSituation), 0, -1):
#     for char in range(0, len(newSituation[line]), 1):
#         print(newSituation[line][char])