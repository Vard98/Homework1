from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

firefox_driver = webdriver.Firefox()
firefox_driver.get("https://www.demoblaze.com/")

try:
    header_element = firefox_driver.find_element(By.XPATH, '//*[@id="navbarExample"]/ul/li[1]/a')
    print("Element is located:", header_element)
except NoSuchElementException:
    print("No Such Element")


try:
    header_element = firefox_driver.find_element(By.CLASS_NAME, "nav-link")
    print("Element is located:", header_element)
except NoSuchElementException:
    print("No Such Element")

try:
    header_element = firefox_driver.find_element(By.LINK_TEXT, "About")
    print("Element is located:", header_element)
except NoSuchElementException:
    print("No Such Element")

firefox_driver.quit()
