from selenium import webdriver


firefox_driver = webdriver.Firefox()
firefox_driver.get("https://www.demoblaze.com/")
firefox_driver.save_screenshot("C:\\Users\\USER\\Pictures\\Screenshots\\firefox_screen.png")
firefox_driver.quit()
edge_driver = webdriver.Edge()
edge_driver.get("https://www.demoblaze.com/")
edge_driver.save_screenshot("C:\\Users\\USER\\Pictures\\Screenshots\\edge_screen.png")
edge_driver.quit()
