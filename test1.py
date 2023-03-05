import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

edge_driver = webdriver.Edge()


class TestingPages:
    def test_radio_buttons(self):
        global edge_driver
        edge_driver.get("https://courses.letskodeit.com/practice")
        wait = WebDriverWait(edge_driver, 30)
        bmw_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id = 'bmwradio']")))
        assert not bmw_radio.is_selected()
        bmw_radio.click()
        benz_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzradio']")))
        honda_radio = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondaradio']")))
        assert bmw_radio.is_selected()
        assert not benz_radio.is_selected()
        assert not honda_radio.is_selected()
        benz_radio.click()
        assert benz_radio.is_selected()
        assert not bmw_radio.is_selected()
        assert not honda_radio.is_selected()
        honda_radio.click()
        assert honda_radio.is_selected()
        assert not bmw_radio.is_selected()
        assert not benz_radio.is_selected()

    def test_checkbox_buttons(self):
        global edge_driver
        edge_driver.get("https://courses.letskodeit.com/practice")
        wait = WebDriverWait(edge_driver, 30)
        bmw_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='bmwcheck']")))
        assert not bmw_checkbox.is_selected()
        bmw_checkbox.click()
        benz_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzcheck']")))
        honda_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondacheck']")))
        assert not benz_checkbox.is_selected()
        assert not honda_checkbox.is_selected()
        benz_checkbox.click()
        assert not honda_checkbox.is_selected()
        honda_checkbox.click()
        assert bmw_checkbox.is_selected()
        assert benz_checkbox.is_selected()
        assert honda_checkbox.is_selected()
        # AfterRefresh
        edge_driver.refresh()
        bmw_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='bmwcheck']")))
        benz_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzcheck']")))
        honda_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondacheck']")))
        assert not bmw_checkbox.is_selected()
        assert not honda_checkbox.is_selected()
        benz_checkbox.click()
        # AfterSecondRefresh
        edge_driver.refresh()
        bmw_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='bmwcheck']")))
        benz_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='benzcheck']")))
        honda_checkbox = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='hondacheck']")))
        assert not bmw_checkbox.is_selected()
        assert not benz_checkbox.is_selected()
        honda_checkbox.click()

    def test_dropdown(self):
        global edge_driver
        edge_driver.get("https://courses.letskodeit.com/practice")
        wait = WebDriverWait(edge_driver, 30)
        cars = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'select[id="carselect"]')))
        cars_select = Select(cars)
        cars_select.select_by_index(2)
        cars_select.select_by_visible_text("Benz")
        cars_select.select_by_value("bmw")

    def test_mouse_hover(self):
        global edge_driver
        edge_driver.get("https://courses.letskodeit.com/practice")
        wait = WebDriverWait(edge_driver, 30)
        input_name = "Fred"
        input_field = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[id="name"]'))).send_keys(input_name)
        mouse_hover = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="mousehover"]')))
        mouse_hover.click()
        actions = ActionChains(edge_driver)
        actions.move_to_element(mouse_hover).perform()
        test_reload = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div[class="mouse-hover-content"] > a:nth-child(2)')))
        test_reload.click()
        assert not input_field == input_name




