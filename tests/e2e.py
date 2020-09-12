#!/usr/bin/env python3
from selenium import webdriver
import sys


# function to retrieve number from the score element in the provided webpage and check if it's between 0 and 1000. Return a boolean value on the result.
def test_scores_service(app_url):
    # setting initial return state to False. Will turn to True only if conditions are met without exception errors.
    is_score_valid = False

    # score element xpath
    score_element = '//*[@id="score"]'

    options = webdriver.ChromeOptions()
    # below options are for running the webdriver in a docker container
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument("--headless")

    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)

    # using "try" to get to return regardless of the exception type
    try:
        driver.get(app_url)
        score = driver.find_element_by_xpath(score_element).text
        if int(score) >= 0 and int(score) <= 1000:
            is_score_valid = True
    except Exception as e:
        print(e)
    driver.quit()
    return is_score_valid

def main_function():
    app_url = 'http://0.0.0.0:8777/'
    if test_scores_service(app_url) == True:
        sys.exit(0)
    else:
        sys.exit(-1)
    return

if __name__ == "__main__":
    main_function()
