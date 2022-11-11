# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月01日
'''
from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Testwait():
    def setup(self):
        # Chrome实例化的时候需要加一个option，否则会报错提示：不是w3c标准的命令
        option = webdriver.ChromeOptions()
        # 需要另外设置一个参数 add_experimental_option，传进来一个name和value
        option.add_experimental_option('w3c', False)
        self.driver = webdriver.Chrome(options=option) # 把option对象添加到Chrome中
        self.driver.maximize_window() # 浏览器页面最大化
        self.driver.implicitly_wait(5) # 隐式等待

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        self.driver.get("https://ceshiren.com/latest")
        # 找到元素 所有分类并且点击
        self.driver.find_element(By.XPATH,'//*[@title="所有分类"]').click()

        # 第一种：自定义显示等待

        # 2.自己定义一个方法（函数）
        def wait(x): # 一定要传一个参数，用来接参，因为下边的 until 调用wait的时候，把self.driver传给了这个参数
            # return可以返回一个长度，如果找到了>=1个元素，就执行后边的语句
            return len(self.driver.find_elements(By.XPATH,'//*[@class="table-heading"]')) >=1
        # 3.把自己定义的函数传进来   python传参的时候，不要写()，下边这个wait后边不写()
        WebDriverWait(self.driver, 5).until(wait)# 1.声明一个显示等待，需要传一个参数(deiver和等待时间).until()是条件，需要传一个方法进来
        self.driver.find_element(By.XPATH,'//*[@class="category-name"]').click()


        # 第二种：selenium自带的  3种等待方法

        # expected_conditions.element_to_be_clickable() # 等待 直到元素可被点击 1
        # expected_conditions.visibility_of_element_located() # 等待 直到元素可见 2
        # expected_conditions.presence_of_element_located() # 等待 直到元素出现 3
        # expected_conditions.title_is() # 等待 标题是什么

        # expected_conditions.element_to_be_clickable() # 点击进去看源码详解
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="table-heading"]')))
        # WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@class="active"]')))
        # WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@class="active"]')))
        # 上边执行过了，才会执行下边的
        # 滑动到底部，找到 更多
        el = self.driver.find_element(By.XPATH, '//*[@class="table-heading"]')
        action = TouchActions(self.driver)
        action.scroll_from_element(el, 0,5000).perform()
        # action.scroll(0,5000).perform()
        self.driver.find_element(By.XPATH, '//*[@id="ember157"]/div/div/div[1]/div[1]')
        # 滑动到页面顶部
        self.driver.execute_script('document.documentElement.scroll=0')

