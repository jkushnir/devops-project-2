#!/usr/bin/env python3

from Live import load_game, welcome
from Utils import screen_cleaner

# setting initial player_won state for the while loop to run
player_won = False

print(welcome("Yevgeny"))
#clearing the screen and re-loading the game until player wins
while not player_won:
    screen_cleaner()
    player_won = load_game()

