#!/usr/bin/env python3
import os

SCORES_FILE_NAME = 'Scores.txt'
ERROR_MESSAGE = 'Something went wrong...'

# sends relevant clear screen command depending on the OS.
def screen_cleaner():
    os.system('cls' if os.name =='nt' else 'clear')

# input number validator, receives number to validate and acceptable number range list, e.g. [1,10].
def validate_number(value, number_range):
    try:
        number = int(value)
    except ValueError:
        value_is_valid = False
    else:
        if number_range[0] <= number <= number_range[1]:
            value_is_valid = True
        else:
            value_is_valid = False
    return value_is_valid
