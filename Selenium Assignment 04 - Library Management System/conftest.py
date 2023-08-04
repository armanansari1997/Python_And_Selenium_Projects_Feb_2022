import pytest
from selenium import webdriver


@pytest.fixture
def chrome_driver():
    # Arrange
    driver = webdriver.Chrome(executable_path='D://Drivers/chromedriver.exe')
    driver.maximize_window()
    # implicit wait is applicable for element/elements only
    # It is a global wait
    driver.implicitly_wait(20)
    # Cleanup
    yield driver
    driver.quit()
