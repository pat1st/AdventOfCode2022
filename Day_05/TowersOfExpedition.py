import numpy as np
file1 = open('Day_05\inputProd.txt', 'r')
fileFull = file1.read()

situation, actions = fileFull.split('\n\n')
print(situation)

situation = situation.split('\n')
situMatrixFull = np.array([list(x) for x in situation])
situMatrixTarget = np.empty(
    (situMatrixFull.shape[0]-1, int((situMatrixFull.shape[1]+2)/4)), str)
print('Matrix:', situMatrixTarget.shape[0], situMatrixTarget.shape[1])

for line in range(1, situMatrixFull.shape[1], 4):
    stack = situMatrixFull[0:situMatrixFull.shape[0]-1, line]
    situMatrixTarget[0:situMatrixFull.shape[0], int(line/4)] = stack

print(situMatrixTarget)  # 2D array of the situation

towArr = []
for stack in range(0, situMatrixTarget.shape[0]+1):
    stackArr = []
    for pos in range(situMatrixTarget.shape[1]-2, -1, -1):
        value = situMatrixTarget[pos, stack]
        print(value, stack, pos)
        if value != ' ':
            stackArr.append(value)
    towArr.append(stackArr)

print(towArr)

actions = actions.split('\n')
for action in actions:
    print(action)
    actionSteps = action.replace('move ', '').replace(
        ' from ', ';').replace(' to ', ';').split(';')
    for step in range(0, int(actionSteps[0])):
        crate = towArr[int(actionSteps[1])-1].pop()
        towArr[int(actionSteps[2])-1].append(crate)
    print(towArr)

# Output:
out = ''
for arr in towArr:
    out += arr.pop()
print(out)