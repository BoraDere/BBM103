import sys
y = int(sys.argv[1])
n = int(sys.argv[2])
myNum = y**n


def sumOfDigits(a):
    x = sum(int(digit) for digit in str(a))
    if x < 10:
        global myNum
        myNum = [int(x) for x in str(myNum)]
        print(str(myNum).replace(", ", " + ")[1:-1] + " = " + str(x))
    else:
        myNum = [int(x) for x in str(myNum)]
        print(str(myNum).replace(", ", " + ")[1:-1] + " = " + str(x), end=" = ")
        myNum = x
        sumOfDigits(myNum)


if y < 0 or n < 0:
    pass
else:
    print(str(y) + "^" + str(n) + " = " + str(y ** n), end=" = ")
    sumOfDigits(myNum)