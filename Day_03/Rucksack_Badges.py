file1 = open('Day_03\inputProd.txt', 'r')
Lines = file1.readlines()

itemPriority = {}
for i in range(26):
	itemPriority[chr(97+i)] = i+1
for i in range(26):
	itemPriority[chr(97-32+i)] = i+1+26

#print(itemPriority)

prioSum = 0

for i in range(0, len(Lines), 3):
	for x in Lines[i]:
		if x in Lines[i+1]:
			if x in Lines[i+2]:
				prioSum += itemPriority[x]
				print(x, itemPriority[x], prioSum)
				break

print(prioSum)