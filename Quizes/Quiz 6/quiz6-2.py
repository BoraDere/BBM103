import sys


def diamond_printer(n):
    l = ["*" * j for j in range(1, 2*n) if j % 2 == 1]
    width = 2 * n - 1
    for k in range(0, number):
        print(l[k].center(width, " "))
    l.reverse()
    for z in range(1, number):
        print(l[z].center(width, " "))


number = int(sys.argv[1])
diamond_printer(number)
