from time import sleep
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLitemall:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    @allure.story('新增功能')
    def test_new(self):

        # 登录后台系统
        self.driver.get('https://litemall.hogwarts.ceshiren.com/#/login')
        # 遇到问题：输入框内有默认值，此时send_keys不会清空输入框，只会追加，所以需要先清空输入框，再输入用户名和密码
        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'username').send_keys('manage')
        self.driver.find_element(By.NAME, 'password').clear()
        self.driver.find_element(By.NAME, 'password').send_keys('manage123')
        self.driver.find_element(By.CSS_SELECTOR, '.el-button--primary').click()
        sleep(1)

        # 进入商品类目页面
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()

        # 添加商品类目
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys('1013新增的商品')
        self.driver.find_element(By.CSS_SELECTOR, ".el-icon-arrow-up").click() # 点击’级别‘下拉框
        self.driver.find_element(By.XPATH, "//body/div[3]//li[1]/span").click() # 点击’一级类目‘枚举值
        self.driver.find_element(By.XPATH, "//*[text()='确定']").click() # 点击确定

        # 断言 是否新增成功
        # finds 如果没找到会返回空列表， find 如果没找到会直接报错
        # 正常情况下，如果没有找到，也不应该报错
        res = self.driver.find_elements(By.XPATH, '//*[text()="1013新增的商品"]')
        # 断言新增后是否能找到，如果找到，说明新增成功
        # 判断查找的结果是否为空列表，如果为空列表则说明没找到
        assert res != []


    @allure.story('删除功能')
    def test_delete(self):
        allure.step('第一步：【造数据】')
        # 登录后台系统
        self.driver.get('https://litemall.hogwarts.ceshiren.com/#/login')
        # 遇到问题：输入框内有默认值，此时send_keys不会清空输入框，只会追加，所以需要先清空输入框，再输入用户名和密码
        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'username').send_keys('manage')
        self.driver.find_element(By.NAME, 'password').clear()
        self.driver.find_element(By.NAME, 'password').send_keys('manage123')
        self.driver.find_element(By.CSS_SELECTOR, '.el-button--primary').click()
        sleep(1)

        # 进入商品类目页面
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()

        # 添加商品类目
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys('1013删除的商品')
        self.driver.find_element(By.CSS_SELECTOR, ".el-icon-arrow-up").click() # 点击’级别‘下拉框
        self.driver.find_element(By.XPATH, "//body/div[3]//li[1]/span").click() # 点击’一级类目‘枚举值
        self.driver.find_element(By.XPATH, "//*[text()='确定']").click() # 点击确定

        # 删除
        allure.step('第二步：【删除数据】')
        self.driver.find_element(By.XPATH, "//*[text()='1013删除的商品']/../..//*[text()='删除']").click()
        sleep(1)

        # 断言 是否删除成功     ***注意：这是 elements
        res = self.driver.find_elements(By.XPATH, "//*[text()='1013删除的商品']")
        assert res == []
