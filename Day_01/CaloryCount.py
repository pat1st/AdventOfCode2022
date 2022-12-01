file1 = open('Day_01\inputProd.txt', 'r')
Lines = file1.readlines()
  
count = 0
mymax = 0
# Strips the newline character
for line in Lines:
    if  line.strip() == '':
        if count > mymax:
            mymax = count
        count = 0
    else:
        # add line as int
        count += int(line.strip())

print(mymax)