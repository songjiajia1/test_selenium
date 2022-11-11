import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
import sys
sys.path.append("../..")
from test_01_jichu.utils.log.log_util import logger

'''问题一、用例产生了脏数据
解决方案：清理对应的脏数据，清理的方式可以用接口或者UI的方式，    数据的清理一定要放在断言后边，否则可能会影响断言结果
    问题二、代码存在大量的强制等待
解决方案：使用显示等待优化
****** 很多代码重复，维护困难。学习完PO设计模式之后可以解决这些问题 ******
'''

class TestLitemall:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

        # 登录后台系统
        self.driver.get('https://litemall.hogwarts.ceshiren.com/')
        # 遇到问题：输入框内有默认值，此时send_keys不会清空输入框，只会追加，所以需要先清空输入框，再输入用户名和密码
        self.driver.find_element(By.NAME, 'username').clear()
        self.driver.find_element(By.NAME, 'username').send_keys('manage')
        self.driver.find_element(By.NAME, 'password').clear()
        self.driver.find_element(By.NAME, 'password').send_keys('manage123')
        self.driver.find_element(By.CSS_SELECTOR, '.el-button--primary').click()

    def teardown_class(self):
        self.driver.quit()

    # 获取截图
    def get_screenshot(self):
        timestamp = int(time.time())
        # 要提前创建好 images 路径
        image_path = f'../images/image_{timestamp}.PNG'
        # 截图
        self.driver.save_screenshot(image_path)
        # 将截图放到测试报告中    文件路径    名称                          格式
        allure.attach.file(image_path, name='picture', attachment_type=allure.attachment_type.PNG)

    @allure.story('新增功能')
    def test_new(self):

        # 进入商品类目页面
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()

        # 添加商品类目
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys('1013新增的商品')
        self.driver.find_element(By.CSS_SELECTOR, ".el-icon-arrow-up").click() # 点击’级别‘下拉框
        self.driver.find_element(By.XPATH, "//body/div[3]//li[1]/span").click() # 点击’一级类目‘枚举值
        # 下边这行是优化前的写法，就是不用显示等待的写法
        # self.driver.find_element(By.XPATH, "//*[text()='确定']").click() # 点击确定
        '''===== 使用显示等待优化 方案1 ==== 调用 expected_conditions'''
        # WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[text()='确定']"))).click() # 点击确定
        '''===== 显示等待优化 方案2 ==== 自定义显示等待'''
        def click_exception(by, element, max_attempts=5): # 最大点击次数
            def _inner(driver):
                # 多次点击按钮
                actul_attempts = 0 # 实际点击次数
                while actul_attempts<max_attempts:
                    actul_attempts += 1 # 每次循环，实际点击次数都要 + 1
                    try:
                        # 如果点击过程中报错，则直接执行 except Exception 这个逻辑，并且继续执行循环操作
                        driver.find_element(by, element).click()
                        # 如果点击成功，则直接return，并结束循环
                        return True
                    except Exception:
                        logger.debug('此次点击没有成功')
                # 当实际点击次数 大于 最大点击次数时，结束循环并抛出异常
                raise Exception('超出了最大点击次数')
            return _inner
        WebDriverWait(self.driver, 5).until(click_exception(By.XPATH, "//*[text()='确定']"))

        # 断言 是否新增成功
        # finds：如果没找到会返回空列表， find：如果没找到会直接报错
        # 正常情况下，如果没有找到，也不应该报错
        res = self.driver.find_elements(By.XPATH, '//*[text()="1013新增的商品"]')
        self.get_screenshot() # 获取截图
        '''清理数据''' # 数据的清理一定要放在断言后边，否则可能会影响断言结果
        self.driver.find_element(By.XPATH, "//*[text()='1013新增的商品']/../..//*[text()='删除']").click()
        logger.info(f'断言获取到的实际结果为{res}')
        # 判断新增后是否能找到，如果找到，说明新增成功
        # 判断查找的结果是否为空列表，如果为空列表则说明没找到
        assert res != []


    @allure.story('删除功能')
    def test_delete(self):

        # 进入商品类目页面
        self.driver.find_element(By.XPATH, "//*[text()='商场管理']").click()
        # self.driver.find_element(By.XPATH, "//*[text()='商品类目']").click()
        # WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[text()='商品类目']"))).click()
        def aaa(by, element, _max=5):
            def bbb(driver):
                _min = 0
                while _min < _max:
                    _min += 1
                    try:
                        driver.find_element(by, element).click()
                        return True
                    except Exception:
                        logger.debug('此次点击没有成功')
                raise Exception('超出了最大点击次数')
            return bbb
        WebDriverWait(self.driver, 10).until(aaa(By.XPATH, "//*[text()='商品类目']"))

        # 添加商品类目
        self.driver.find_element(By.XPATH, "//*[text()='添加']").click()
        self.driver.find_element(By.CSS_SELECTOR, ".el-input__inner").send_keys('1013删除的商品')
        self.driver.find_element(By.CSS_SELECTOR, ".el-icon-arrow-up").click() # 点击’级别‘下拉框
        # self.driver.find_element(By.XPATH, "//body/div[3]//li[1]/span").click() # 点击’一级类目‘枚举值
        '''===== 显示等待优化 方案2 ==== 自定义显示等待'''
        def aaaa(by, element, _max=5):
            def bbbb(driver):
                _min = 0
                while _min < _max:
                    _min += 1
                    try:
                        driver.find_element(by, element).click()
                        return True
                    except Exception:
                        logger.debug('此次点击没有成功')
                raise Exception('超出了最大点击次数')
            return bbbb
        WebDriverWait(self.driver, 5).until(aaaa(By.XPATH, "//body/div[3]//li[1]/span"))
        self.driver.find_element(By.XPATH, "//*[text()='确定']").click() # 点击确定

        # 删除
        allure.step('第二步：【删除数据】')
        self.driver.find_element(By.XPATH, "//*[text()='1013删除的商品']/../..//*[text()='删除']").click()

        # 问题：因为代码执行过快，导致元素还未消失就被捕获了，要确认元素不存在后，再捕获和断言
        WebDriverWait(self.driver, 5).until_not(expected_conditions.visibility_of_any_elements_located((By.XPATH, "//*[text()='1013删除的商品']")))
        # 断言 是否删除成功     ***注意：这是 elements
        res = self.driver.find_elements(By.XPATH, "//*[text()='1013删除的商品']")
        self.get_screenshot() # 获取截图
        logger.info(f'断言 获取到的实际结果为{res}')
        assert res == []

'''visibility_of_any_elements_located(要查找的元素)
作用：定位到的是一个列表，在要查找的这个元素的列表中有任意一个定位到的话，就会返回 True
'''
