file1 = open('Day_01\inputProd.txt', 'r')
Lines = file1.readlines()
  
count = 0
myDict = {}
index = 0

for line in Lines:
    if  line.strip() == '':
        myDict [index] = count
        count = 0
        index += 1
    else:
        # add line as int
        count += int(line.strip())
        myDict [index] = count

#get sum of top 3 values of myDict
top3 = sorted(myDict.values(), reverse=True)[:3]
# sum up values in top3
print(sum(top3))
print(top3)