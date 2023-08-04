import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_locator_01():
    # Arrange
    driver = webdriver.Chrome(executable_path='D://Drivers/chromedriver.exe')
    driver.get("https://www.facebook.com")
    username_text = driver.find_element(by=By.ID, value='email')
    password_text = driver.find_element(by=By.ID, value='pass')
    login_btn = driver.find_element(by=By.NAME, value='login')

    # Act
    time.sleep(5)
    username_text.send_keys('hello')
    time.sleep(5)
    password_text.send_keys('hello')
    time.sleep(5)
    login_btn.click()

    # Validate
    title_test = driver.title
    assert title_test == 'Facebook – log in or sign up'

    # Cleanup
    driver.quit()
