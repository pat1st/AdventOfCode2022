import numpy as np
file1 = open('Day_05\inputTest.txt', 'r')
fileFull = file1.read()

situation, actions = fileFull.split('\n\n')
print(situation)

situation = situation.split('\n')
situMatrix = np.array([list(x) for x in situation])
towArr = []

for line in range(1, situMatrix.shape[1], 4):
     np = situMatrix[0:situMatrix.shape[0]-1,line]
     towArr.append(np)

print(towArr)