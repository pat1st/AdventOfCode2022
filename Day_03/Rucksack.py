file1 = open('Day_03\inputProd.txt', 'r')
Lines = file1.readlines()

itemPriority = {}
for i in range(26):
	itemPriority[chr(97+i)] = i+1
for i in range(26):
	itemPriority[chr(97-32+i)] = i+1+26

print(itemPriority)

prioSum = 0

for line in Lines:
	#half the string
	half = int(len(line)/2)
	a,b = line[:half], line[half:]
	print(a,b)
	for i in a:
		if i in b:
			prioSum += itemPriority[i]
			print(i, itemPriority[i], prioSum)
			break

print(prioSum)