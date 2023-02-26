from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

chrome_driver = webdriver.Chrome()
chrome_driver.maximize_window()
chrome_driver.get("https://www.demoblaze.com/")

wait = WebDriverWait(chrome_driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='navbarExample']")))
login = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[id='login2']")))
login.click()
try:
    login_window = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='logInModal']/div/div")))
    print("login button is working")
except NoSuchElementException:
    print("login button doesn't work")
