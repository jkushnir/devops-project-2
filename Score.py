#!/usr/bin/env python3

# trying to read score (integer) from file (creating file if not found/cant
def add_score(points):
    current_score = 0
    try:
        f = open('Scores.txt', 'r+')
        file_content = f.read()
        current_score = int(file_content)
    except (FileNotFoundError, ValueError): # making a new file if file not exist or empty/corrupted
        f = open('Scores.txt', 'w')
    score_sum = str(current_score + points)
    f.seek(0)
    f.write(score_sum)
    f.truncate()
    f.close()


# self test
if __name__ == '__main__':
    add_score(4)
    with open('Scores.txt', 'r') as f:
        print(f.read())
