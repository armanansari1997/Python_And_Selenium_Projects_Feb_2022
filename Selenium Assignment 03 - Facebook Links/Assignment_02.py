import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def test_locator_02():
    # Arrange
    driver = webdriver.Chrome(executable_path='D://Drivers/chromedriver.exe')
    driver.get("https://www.facebook.com")

    # Act
    page_footer_links = driver.find_element(by=By.XPATH, value="//div[@id='pageFooterChildren']/child::ul")
    all_links_list = page_footer_links.find_elements(by=By.TAG_NAME, value='a')

    # Validate
    no_of_links = len(all_links_list)
    print()
    print("****** The number of links are ", no_of_links)
    links_list = []
    for list in all_links_list:
        links_list.append(list.text)
    print("***** The Links list are ******")
    print(links_list)

    # count = 0
    # for link_no in range(no_of_links):
    #     page_footer_links = driver.find_element(by=By.XPATH, value="//div[@id='pageFooterChildren']/child::ul")
    #     all_links_list = page_footer_links.find_elements(by=By.TAG_NAME, value='a')
    #     oldtab = driver.current_window_handle
    #     all_links_list[link_no].click()
    #     time.sleep(3)
    #     title = driver.title
    #     # if title.contains("404"):
    #     #     print("***** Broken link found")
    #     #     count += 1
    #     if driver.current_window_handle != oldtab :
    #         driver.switch_to_window(oldtab)
    #     driver.back()
    #
    # if count == 0:
    #     print("**** No Broken link found")

    # Cleanup
    driver.quit()

    # links = driver.find_elements_by_css_selector("a")
    # for link in links:
    #     r = requests.head(link.get_attribute('href'))
    #     print(link.get_attribute('href'), r.status_code)

    # r = requests.head(link.get_attribute('href'))
    # print(link.get_attribute('href'), r.status_code)
