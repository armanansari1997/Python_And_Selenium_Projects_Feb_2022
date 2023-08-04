import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_auto_suggestion_dropdown():
    # Arrange
    driver = webdriver.Chrome(executable_path='D://Drivers/chromedriver.exe')
    driver.get("https://www.google.com")
    driver.find_element(By.NAME, 'q').send_keys('Npn Training')
    time.sleep(3)
    all_suggestions = driver.find_elements(By.XPATH, '(//ul[@role="listbox"])[1]')
    for items in all_suggestions:
        print(items.text)
    driver.find_element(By.XPATH, '//span[text() = "NPN Training"]').click()
    time.sleep(3)


