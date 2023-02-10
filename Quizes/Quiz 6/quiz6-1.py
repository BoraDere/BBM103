import sys


def diamond_printer(n, row=1):
    width = 2 * number - 1
    if n == 1 - number:
        return
    if n <= 0:
        amount = 2 * (row - 2) - 1
        print(("*" * amount).center(width, " "))
        diamond_printer(n - 1, row - 1)
    else:
        amount = 2 * row - 1
        print(("*" * amount).center(width, " "))
        diamond_printer(n - 1, row + 1)


number = int(sys.argv[1])
diamond_printer(number)
