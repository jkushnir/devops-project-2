#!/usr/bin/env python3

from Utils import validate_number, ERROR_MESSAGE
import MemoryGame
import GuessGame
import Score

# receives variable "name" and returns a welcome message with the name embedded into it.
def welcome(name):
    welcome_message = ("Hello {name} and welcome to the World of Games (WoG).\n"
                       "Here you can find many cool games to play".format(name=name))
    return welcome_message


# asks the user to select game and difficulty, validates selections, loads selected game/difficulty and updates the score file if won
def load_game():
    choose_game_message = ("Please choose a game to play:\n"
                           "    1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                           "    2. Guess Game - guess a number and see if you chose like the computer")
    print(choose_game_message)
    # loop until input passes validation
    while True:
            selected_game = input()
            if validate_number(selected_game, [1,2]):
                break
            else:
                print(ERROR_MESSAGE)
                print("Please enter game number (1 or 2)")

    print("Please choose game difficulty from 1 to 5:")

    # loop until input passes validation
    while True:
            difficulty = input()
            if validate_number(difficulty, [1,5]):
                # casting difficulty as integer to itself
                difficulty = int(difficulty)
                break
            else:
                print(ERROR_MESSAGE)
                print("Please enter game number (1 to 5)")

    if selected_game == '1':
        # play memory game, result goes to player_won
        player_won = MemoryGame.play(difficulty)
        if player_won:
            Score.add_score(difficulty)
    if selected_game == '2':
        # play guess game, result goes to player_won
        player_won = GuessGame.play(difficulty)
        # if result is True, add the difficulty value to the score
        if player_won:
            Score.add_score(difficulty)
    return(player_won)

# self test
if __name__ == "__main__":
    print(welcome('Yevgeny'))
    load_game()

