file1 = open('Day_04\inputProd.txt', 'r')
Lines = file1.readlines()

count = 0

for line in Lines:
	a,b = line.split(',')
	a1,a2 = a.split('-')
	b1,b2 = b.split('-')
	if	(int(a1) >= int(b1) and int(a2) <= int(b2)) or \
		(int(b1) >= int(a1) and int(b2) <= int(a2)):
			count += 1
			print(a,b, count)

print(count)