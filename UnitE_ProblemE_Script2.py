'''
Sanjana Gadaginmath
CIS 41A   Winter 2022
Unit E, Problem E
'''
#Second Script – Guessing Game

import random
secretNum = random.randint(1, 100)
print("Welcome to the guessing game. \nYou need to guess a number from 1 to 100.")
guess = int(input("What is your guess? "))
tries = 1
while guess != secretNum:
    if guess < secretNum:
        print("Guess is too low.")
    elif guess > secretNum:
        print("Guess is too high.")
    guess = int(input("What is your guess? "))
    tries += 1
if guess == secretNum:
    print("Congratulations! \nYou guessed the secret number in {} guesses!".format(tries))
    
'''
Execution results:
Welcome to the guessing game. 
You need to guess a number from 1 to 100.
What is your guess? 50
Guess is too low.
What is your guess? 60
Guess is too low.
What is your guess? 70
Guess is too low.
What is your guess? 80
Guess is too high.
What is your guess? 71
Guess is too low.
What is your guess? 72
Guess is too low.
What is your guess? 73
Guess is too low.
What is your guess? 74
Guess is too low.
What is your guess? 75
Guess is too low.
What is your guess? 76
Congratulations! 
You guessed the secret number in 10 guesses!

