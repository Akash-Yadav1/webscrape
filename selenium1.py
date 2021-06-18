from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.python.org')

assert "Python" in driver.title

elem = driver.find_element_by_name("q")

elem.clear()
elem.send_keys('pycon')
elem.send_keys(Keys.RETURN)

assert "NO result found" in driver.page_source
