import random

random_number = random.randint(1, 20)
guess_count = 0

while (guess_count == 0):
    guess = input("Guess the number, it's between 1 and 20!\n")
    if (guess == random_number):
        guess_count = 1
        print("You are right!!")
    else:
        print("Nope!")