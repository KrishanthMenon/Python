from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://www.google.com')
driver.maximize_window()

input = driver.find_element_by_name('q')
input.send_keys('selenium')
time.sleep(5)

button = driver.find_element_by_class_name('gNO89b')
button.click()