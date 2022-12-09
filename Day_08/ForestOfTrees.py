file1 = open('Day_08\inputProd.txt', 'r')
Lines = file1.readlines()

Forest = []
for line in Lines:
	TreeLine = []
	for i in range(0, len(line)):
		if len(line[i].strip()) != 0:
			TreeLine.append(line[i])
	Forest.append(TreeLine)

print(Forest)

ForestWidth = len(Forest)
ForestHeight = len(Forest[0])
VisibleTrees = 0

def VisibleHorizontaly(x, y, Forest):
	for i in range(0, ForestWidth):
		if x!=i:
			if Forest[i][y] > Forest[x][y]:
				return False
	return True


def VisibleVertically(x, y, Forest):
	for i in range(0, ForestWidth):
		if y != i:
			if Forest[x][i] > Forest[x][y]:
				return False
	return True

VisibleForest = []

for x in range(0, ForestWidth):
	VisibleTreeLine = []
	for y in range(0, ForestHeight):
		print(Forest[x][y], end='')
		VisibleTreeLine.append(' ')
		if x==0 or x==ForestHeight-1 or y==0 or y==ForestWidth-1:
			VisibleTrees += 1
			VisibleTreeLine[y] = Forest[x][y]
		elif VisibleHorizontaly(x, y, Forest) or VisibleVertically(x, y, Forest):
			VisibleTrees += 1
			VisibleTreeLine[y] = Forest[x][y]
	print()
	VisibleForest.append(VisibleTreeLine)
print(VisibleTrees)

#print(VisibleForest)
for line in VisibleForest:
	for i in range(0, len(line)):
		print(line[i], end='')
	print()

print(VisibleTrees)
