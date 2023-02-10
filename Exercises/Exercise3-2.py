import random
number = random.randint(1, 25)
guess = 0
while guess != number:
    guess = int(input("Guess a number between 1 and 25: "))
    while guess > number:
        guess = int(input("Decrease your number: "))
    while guess < number:
        guess = int(input("Increase your number: "))
    if guess == number:
        print("You won!")
