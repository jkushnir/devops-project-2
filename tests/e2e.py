#!/usr/bin/env python3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 
import time
import os
import sys
from datetime import datetime
import logging


app_url = 'http://0.0.0.0:8777/'


options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
#options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

def test_scores_service(app_url):
    score_element = '//*[@id="score"]'
    score_valid = False
    try:
        driver.get(app_url)
        score = driver.find_element_by_xpath(score_element)
        if (int(score) > 0) or (int(score < 1000):
            score_valid = True
            print('success!!!')
    except Exception as e:
        print(e)
        driver.quit()
    driver.quit()
driver.quit()
    return score_valid

def main_function():
    return os_code

if __name__ == "__main__":
    main_function()
