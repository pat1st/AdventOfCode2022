file1 = open('Day_06\inputProd.txt', 'r')
fileFull = file1.read()

pos = 0
found = False
def checkForSame(subSignal):
    print(subSignal)
    myDict = {}
    for i in subSignal:
        if i in myDict:
            return True
        else:
            myDict[i] = 1
    return False

while pos < len(fileFull) and not found:
    subSignal = fileFull[pos:pos+14]    
    multi = checkForSame(subSignal)
    if not multi:
        found = True
    pos += 1

print(pos+13)


# zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw
