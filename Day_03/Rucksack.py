file1 = open('Day_03\inputTest.txt', 'r')
Lines = file1.readlines()

itemPriority = {}
for i in range(26):
	itemPriority[chr(97+i)] = i+1
for i in range(26):
	itemPriority[chr(97-32+i)] = i+1+26

print(itemPriority)

for line in Lines:
	#half the string
	half = int(len(line)/2)
	a,b = line.split()