from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCeshiren:

    def setup(self):
        # 1.打开浏览器
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        # 2.打开被测地址
        self.driver.get('https://ceshiren.com/search?expanded=true')

    def teardown(self):
        self.driver.quit()

    def test_search(self):
        # 3.定位到搜索输入框，并输入搜索内容
        self.driver.find_element(By.CSS_SELECTOR, '[placeholder="搜索"]').send_keys('appium')
        # 4.定位搜索按钮并点击
        self.driver.find_element(By.CSS_SELECTOR, '.search-cta').click()
        # 5.断言 预期结果=实际结果
        # 获取实际结果
        web_element = self.driver.find_element(By.CSS_SELECTOR, '.search-link')
        # 断言输入的内容，是否在获取的实际结果的文本之中
        assert 'appium' in web_element.text.lower() # lower() 把获取到的内容全部小写或者输入的内容大写也行
