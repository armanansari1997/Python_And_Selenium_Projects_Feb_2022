import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def test_exercise_01(chrome_driver):
    chrome_driver.get('https://www.npntraining.com/projects/selenium/hosted/Library%20Management%20System/librarian/')
    chrome_driver.find_element(By.ID, 'username').send_keys('admin')
    chrome_driver.find_element(By.ID, 'password').send_keys('admin1234')
    chrome_driver.find_element(By.ID, 'login').click()

    options = webdriver.ChromeOptions()
    options.add_argument('disable-notifications')

    chrome_driver.find_element(By.XPATH, '//a[contains(text(),"Users")]').click()
    chrome_driver.find_element(By.XPATH, '(//strong[text()="Add User"])[1]').click()

    chrome_driver.find_element(By.XPATH, '(//input[@name="username"])[1]').send_keys('arman')
    chrome_driver.find_element(By.XPATH, '(//input[@name="password"])[1]').send_keys('arman1234')
    chrome_driver.find_element(By.XPATH, '(//input[@name="firstname"])[1]').send_keys('Arman')
    chrome_driver.find_element(By.XPATH, '(//input[@name="lastname"])[1]').send_keys('Ansari')
    chrome_driver.find_element(By.NAME, 'submit').click()

    assert chrome_driver.find_element(By.XPATH, '//tbody/tr[3]/td[1]').text == 'arman'
