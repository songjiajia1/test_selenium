from selenium import webdriver
from test_01_jichu.conftest import wen_env
import sys
import os.path
print(os.path.abspath('./'))

class TestBrowser:

    def setup_class(self):
        self.browser = wen_env.get('browser')

    def test_browser(self):
        if self.browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com/')
        self.driver.quit()
