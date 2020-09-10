#!/usr/bin/env python3
from Utils import screen_cleaner
import random
import time
from Utils import validate_number
## put validator in Utils

# generating a list with random numbers, number of items is per received difficulty value. Then, showing the list to user for a short time and clearing screen
def generate_sequence(difficulty):
    numbers_list = []
    for i in range(difficulty):
        numbers_list.append(random.randint(1,101))
    print(numbers_list)
    time.sleep(0.7)
    screen_cleaner()
    return numbers_list

# prompting user to enter numbers, validating each number, receiving number of items as per received difficulty value.
def get_list_from_user(difficulty):
    print('After seeing the numbers enter the numbers you saw, each one separated with Enter.')
    remembered_list = []
    for i in range(difficulty):
        while True:
            remembered_number = input()
            if validate_number(remembered_number, [1,101]):
                remembered_list.append(int(remembered_number))
                break
            else:
                print("Number should be from 1 to 101, try again:")
    return remembered_list

# comparing two received lists, ignoring the order. returning comparison result (True / False)
def is_list_equal(list_a, list_b):
    return sorted(list_a) == sorted(list_b)

# main function, generating numbers secquence, then getting numbers list from user, then comparing the two and returning the result.
def play(difficulty):
    list_a = generate_sequence(difficulty)
    list_b = get_list_from_user(difficulty)
    return is_list_equal(list_a, list_b)

# internal test
if __name__ == '__main__':
    print('testing at difficulty 2')
    print(play(2))
