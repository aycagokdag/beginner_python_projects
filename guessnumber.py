import random


guess_count = 0
limit = -1

while (limit < 0):
    limit = int(input('Enter an up limit that is greater than 0: '))
random_number = random.randint(1, limit)
print('')
print(f'I chose a number between 1 and {limit}! Guess the number :)')

while (guess_count == 0):
    guess = int(input())
    print('Enter a valid number.')
    if (guess == random_number):
        guess_count = 1
        print("You are right!!")
    elif(guess < random_number):
        print("Nope! Try something bigger.")
    else:
        print("Nope! Try something smaller.")
