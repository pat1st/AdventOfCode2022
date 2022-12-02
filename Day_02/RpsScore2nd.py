#A = Rock = 1
#B = Paper = 2
#C = Scissors = 3
#X = lose: 0
#Y = draw: 3
#Z = win: 6

myDict = {"A X": 3, "B X": 1, "C X": 2, "A Y": 4, "B Y": 5, "C Y": 6,
          "A Z": 8, "B Z": 9, "C Z": 7}

file1 = open('Day_02\inputProd.txt', 'r')
Lines = file1.readlines()

count = 0
for line in Lines:
    if line.strip() != '':
        print(myDict[line.strip()])
        count += myDict[line.strip()]

print(count)