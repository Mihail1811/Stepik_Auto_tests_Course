import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

def calc(x: str) -> int:
    return math.log(abs(12*math.sin(int(x))))

try:
    button1 = browser.find_element(By.CLASS_NAME, 'trollface').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = browser.find_element(By.ID, 'input_value').text
    res = calc(x)
    input = browser.find_element(By.XPATH, '//input[@type="text"]')
    input.send_keys(res)
    button2 = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
finally:
    time.sleep(3)
    browser.quit()