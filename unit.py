import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get('http://www.python.org')
        self.assertIn('Python', driver.title)
        elm = driver.find_element_by_name('q')
        elm.clear()
        elm.send_keys('pycon')
        elm.send_keys(Keys.RETURN)
        assert "NO resut found" not in driver.page_source

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
