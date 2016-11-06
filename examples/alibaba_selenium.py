from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.firefox.webdriver import FirefoxProfile


start_url = 'https://www.alibaba.com/catalogs/products/CID100009383----------------------------L--------------------------Pharmaceuticals'

driver = webdriver.Firefox()


def get_items(url):
    driver.get(url)
    items = driver.find_elements_by_css_selector('.m-product-item')
    for item in items:
        title = item.find_element_by_css_selector('h2')
        print title.text

    next_button = driver.find_element_by_css_selector('a.next')
    if next_button:
        get_items(next_button.get_attribute('href'))


get_items(start_url)
