import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time


current_dir = os.path.dirname(__file__)
file_path = os.path.join(current_dir, 'file.txt')


browser = webdriver.Chrome()
link = "http://suninjuly.github.io/file_input.html"
browser.get(link)


try:
    first_name = browser.find_element(By.TAG_NAME, 'input')
    first_name.send_keys('Михаил')
    last_name = browser.find_element(By.NAME, 'lastname')
    last_name.send_keys('Жиганов')
    email = browser.find_element(By.NAME, 'email')
    email.send_keys('mihail@gmail.com')
    btn_file = browser.find_element(By.CSS_SELECTOR, 'input[type="file"]')
    btn_file.send_keys(file_path)
    button = browser.find_element(By.XPATH, '//button[@type="submit"]')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
    