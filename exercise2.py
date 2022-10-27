def DecimalToBinary(num):
    if num >= 1:
        DecimalToBinary(num // 2)
    print(num % 2, end='')
DecimalToBinary(int(input("Enter a number: ")))