from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get("https://www.demoblaze.com/")

try:
    categories = driver.find_element(By.CSS_SELECTOR, '.list-group-item#itemc')
    print('Element is located')
except NoSuchElementException:
    print("No Such Element")

try:
    categories = driver.find_element(By.CSS_SELECTOR, 'a[onclick="byCat(\'notebook\')"]')
    print("Element is located")
except NoSuchElementException:
    print("No Such Element")

try:
    categories = driver.find_element(By.CSS_SELECTOR, 'a#itemc')
    print("Element is located")
except NoSuchElementException:
    print("No Such Element")

driver.quit()
