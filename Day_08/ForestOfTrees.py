file1 = open('Day_08\inputTest.txt', 'r')
Lines = file1.readlines()

Forest = []
for line in Lines:
	TreeLine = []
	for i in range(0, len(line)):
		if len(line[i].strip()) != 0:
			TreeLine.append(line[i])
	Forest.append(TreeLine)

print(Forest)

for x in range(0, len(Forest)):
	for y in range(0, len(Forest[x])):
		print(Forest[x][y], end='')
	print()