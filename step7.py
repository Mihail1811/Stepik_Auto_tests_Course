import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import math


def calc(x) -> str:
    return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/get_attribute.html')


try:
    value = browser.find_element(By.ID, 'treasure')
    x = value.get_attribute('valuex')
    
    res = calc(x)
    
    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(res)
    
    checkbox = browser.find_element(By.ID, 'robotCheckbox')
    checkbox.click()
    
    radiobutton = browser.find_element(By.ID, 'robotsRule')
    radiobutton.click()
    
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()
finally:
    time.sleep(5)
    browser.quit()
    