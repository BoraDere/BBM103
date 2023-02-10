myDict = {}
N = int(input("Enter the N value: "))
for i in range(1, N+1):
    myDict[i] = ["*"]*int(i)
print(myDict)