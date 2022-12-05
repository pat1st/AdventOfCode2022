import numpy as np
file1 = open('Day_05\inputTest.txt', 'r')
fileFull = file1.read()

situation, actions = fileFull.split('\n\n')
print(situation)

situation = situation.split('\n') 
situMatrixFull = np.array([list(x) for x in situation]) 
situMatrixTarget = np.empty(
    (situMatrixFull.shape[0]-1, int(situMatrixFull.shape[1]/3)), str)
print('Matrix:', situMatrixTarget.shape[0], situMatrixTarget.shape[1])

for line in range(1, situMatrixFull.shape[1], 4):
    stack = situMatrixFull[0:situMatrixFull.shape[0]-1, line]
    situMatrixTarget[0:situMatrixFull.shape[0], int(line/4)] = stack

print(situMatrixTarget) # 2D array of the situation

towArr = []
for stack in range(0, situMatrixTarget.shape[1]):
    stackArr = []
    for pos in range(situMatrixTarget.shape[0]-1, 0, -1):
        value = situMatrixTarget[pos, stack]
        if value != ' ':
            stackArr.append(value)
    towArr.append(stackArr)

print(towArr)
