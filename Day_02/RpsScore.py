#A = X = Rock = 1
#B = Y = Paper = 2
#C = Z = Scissors = 3
# X 1
# Y 2
# Z 3
#lose: 0
#draw: 3
#win: 6

myDict = {"A X": 4, "B X": 1, "C X": 7, "A Y": 8, "B Y": 5, "C Y": 2,
          "A Z": 3, "B Z": 9, "C Z": 6}

file1 = open('Day_02\inputProd.txt', 'r')
Lines = file1.readlines()

count = 0
for line in Lines:
    if line.strip() != '':
        print(myDict[line.strip()])
        count += myDict[line.strip()]

print(count)