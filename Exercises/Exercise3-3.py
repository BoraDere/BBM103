#n = int(input("Enter a number: "))
#myDict = {}
#for i in range(1, n+1):
#    myDict[i] = i
#columnList = ['S', 'A', 'D']
#columnDict = {}
#for i in range(1, 4):
#    columnDict[i] = columnList[i-1]

# I tried to do it by using dictionary but I stucked there. Tried a few things but could not manage to do that.


def towerOfHanoi(x, initial, final, auxiliary):
    if x == 1:
        print("Move disk 1 from" + initial + " to " + final)
        return
    towerOfHanoi(x - 1, initial, auxiliary, final)
    print("Move disk " + x + " from " + initial + "to " + final)
    towerOfHanoi(x - 1, auxiliary, final, initial)

x = int(input("Enter a number: "))
towerOfHanoi(x, 'I', 'F', 'A')