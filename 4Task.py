from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Edge()
driver.get("https://www.demoblaze.com/")

wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[@id='tbodyid']/div/div/div/h5")))

prices = driver.find_elements(By.XPATH, "//*[@id='tbodyid']/div/div/div/h5")
highest_price = 0
highest_price_name = ""

for price in prices:
    price_value = float(price.text.replace("$", ""))
    if price_value > highest_price:
        highest_price = price_value
        name = price.find_element(By.XPATH, "//*[@id='tbodyid']/div[2]/div/div/h4/a")
        highest_price_name = name.text

print("Highest Price Item: " + highest_price_name + " - ($" + str(highest_price) + ")")
driver.quit()
