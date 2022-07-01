import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

print("HELLO WORLD")

driver = webdriver.Chrome()
driver.get("https://www.google.com")
driver.find_element(By.NAME,"q").send_keys("Hello World")
driver.find_element(By.NAME,"q").submit()
assert 'Hello World' in driver.title
driver.quit()