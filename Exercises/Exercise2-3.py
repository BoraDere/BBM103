myList = [1000, 298, 3579, 100, 200, -45, 900]
myList = sorted(list(myList))
myDict = {}
for i in myList:
    myDict[myList.index(i) + 1] = i
N = int(input("Enter a number: "))
print(myDict[N])