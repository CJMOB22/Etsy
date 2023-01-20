import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


class EtsyTestcase(unittest.TestCase):

    driver = webdriver.Chrome()


    def setUp(self):
        self.browser = webdriver.Chrome()
        self.addCleanup(self.browser.quit)


        def test_signup(self):
        self.browser.get('http://www.etsy.com')
        self.assertIn('Etsy', self.browser.title)
        self.browser.maximize_window()
        time.sleep(5)

        self.browser.find_element(By.CSS_SELECTOR, '.select-signin').click()
        time.sleep(5)

        self.browser.find_element(By.XPATH, '//*[(@id = "wt-modal-container")]').click()
        time.sleep(5)

        elem = self.browser.find_element(By.NAME,'email')
        elem.send_keys("audiohifi22+1@gmail.com")
        time.sleep(5)

        self.browser.find_element(By.NAME, 'name').send_keys("Alex")
        time.sleep(5)

        self.browser.find_element(By.NAME, 'password').send_keys("testing")
        time.sleep(5)

        self.browser.find_element(By.NAME,'submit_attempt').click()
        time.sleep(10)


    def test_login(self):
        self.browser.get('http://www.etsy.com')
        self.assertIn('Etsy', self.browser.title)
        self.browser.maximize_window()
        time.sleep(5)

        self.browser.find_element(By.CSS_SELECTOR, '.select-signin').click()
        time.sleep(5)

        elem = self.browser.find_element(By.NAME, 'email')
        elem.send_keys("audiohifi22@gmail.com")
        time.sleep(5)

        self.browser.find_element(By.NAME, 'password').send_keys("chandu")
        time.sleep(5)

        self.browser.find_element(By.NAME, 'submit_attempt').click()
        time.sleep(10)

    def test_logut(self):

        self.browser.find_element(By.CSS_SELECTOR, '.wt-icon').click()
        time.sleep(5)

        self.browser.find_element(By.CSS_SELECTOR, '.wt-mt-xs-4').click()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()





