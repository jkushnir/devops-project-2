#!/usr/bin/env python3
import random
from Utils import validate_number

# generates random integer from 1 to difficulty number
def generate_number(difficulty):
    return random.randint(1,difficulty)

# receives guessed number from user, validates that it is in requested range (between one and difficulty) and returns the number as integer
def get_guess_from_user(difficulty):
    print("Please guess number from from 1 to {}:".format(difficulty))
    # loop until received number is validated
    while True:
            guessed_number = input()
            if validate_number(guessed_number, [1,difficulty]):
                break
            else:
                print("Number should be from 1 to {}, try again:".format(difficulty))
    return int(guessed_number)

# receiving difficulty and random number, calling get_guess_from_user with the difficulty to receive guessed number and comparing it with the random number. returing comparison result (True/False)
def compare_results(difficulty, secret_number):
    guessed_number = get_guess_from_user(difficulty)
    return guessed_number == secret_number

#main function, generating random number and comparing it with user's guess, returning comparison result (True/False)
def play(difficulty):
    # getting a secret_number
    secret_number = generate_number(difficulty)
    # asking user to guess the number
    return compare_results(difficulty,secret_number)

# internal test
if __name__ == '__main__':
    print('testing at difficulty 2')
    print(play(2))
