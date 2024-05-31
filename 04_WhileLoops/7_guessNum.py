# Guess a number between 1 - 10

import random

n = random.randint(1, 10)       # Here in the parenthesis () we need to enter the range

guess = 0

while guess != n:
    guess = int(input('Guess the number: '))

    if guess < n:
        print('Your guessed number is smaller')

    elif guess > n:
        print('Your guessed number is greater')

    else:
        print('You guessed the right number')