#!/usr/bin/env python3
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys 
import time
import os
import sys
from datetime import datetime
import logging

# elements
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
#options.add_argument("--headless")

driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)

try:
    driver.get(sign_in_url)
    driver.find_element_by_xpath(email_field).send_keys(email)
    driver.find_element_by_xpath(password_field).send_keys(password)
    driver.find_element_by_xpath(login_button).click()
    time.sleep(5)
    html_output = driver.page_source
    if word_to_search in html_output:
        test_passed = True
    else:
        logger.info(text)
except Exception as e:
    logger.info(e)
    logger.info(text)
    driver.quit()
driver.quit()

def main_function():
    


if __name__ == "__main__":
    main_function()
