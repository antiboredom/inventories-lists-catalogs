from selenium import webdriver


start_url = 'https://www.alibaba.com/Pharmaceuticals_pid100009383'

driver = webdriver.Firefox()
driver.get(start_url)

items = driver.find_element_by_css_selector('h2.title')
for item in items:
    print item
