# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月06日
'''

# TouchActions 用法  ---类似于ActionChains
# 可以对H5页面进行操作：点击、滑动、拖拽、多点触控，以及模拟手势的各种操作
import time
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# 例子：打开搜狗，输入内容，点击 搜狗搜索按钮，在搜索结果页从输入框的位置滑动到浏览器底部

class TestTouchActions():
    def setup(self):
        # Chrome实例化的时候需要加一个option，否则会报错提示：不是w3c标准的命令
        option = webdriver.ChromeOptions()
        # 需要另外设置一个参数 add_experimental_option，传进来一个name和value
        option.add_experimental_option('w3c', True)
        self.driver = webdriver.Chrome(options=option) # 把option对象添加到Chrome中
        self.driver.maximize_window() # 浏览器页面最大化
        self.driver.implicitly_wait(5) # 隐式等待

    def teardown(self):
        self.driver.quit()


    @pytest.mark.skip
    # selenium 4.0.0 版本以上就不能用 TouchActions
    def test_touchaction(self):
        self.driver.get('https://www.sogou.com/')
        el = self.driver.find_element(By.ID, 'query').send_keys('selenium') #  # 1.找到输入框输入内容
        el_search = self.driver.find_element(By.ID, 'stb') # 2.找到搜索按钮
        action = TouchActions(self.driver)
        action.tap(el_search) # 4.调用tap方法，点击搜索按钮
        action.perform()
        # 滑动偏移量 x y
        action.scroll_from_element(el, 0,5000).perform() # 滑动，x是0不滑动，y滑动5000，从el，也就是输入框开始滑
        # action.scroll(100,5000).perform() # 这种写法也行
        self.driver.find_element(By.ID, '#sogou_next').click() # 点击底部的 下一页
        time.sleep(2)


    @pytest.mark.skip
    def test_ActionChains(self):
        self.driver.get('https://www.sogou.com/')
        self.driver.find_element(By.ID, 'query').send_keys('selenium') # 1.找到输入框输入内容
        self.driver.find_element(By.ID, 'stb').click() # 2.找到搜索按钮并点击
        time.sleep(2)
        # ele = self.driver.find_element(By.XPATH, '//*[text()="相关搜索"]') # 定位要滑动到的元素
        # ActionChains(self.driver).scroll_to_element(ele).perform() # 滑动到定位的元素
        ActionChains(self.driver).scroll_by_amount(0, 5000).perform()
        time.sleep(2)

    @pytest.mark.skip
    def test_aaa(self):
        self.driver.get('https://ceshiren.com/')
        # ActionChains(self.driver).scroll_by_amount(0, 5000).perform()
        ele = self.driver.find_element(By.XPATH, '//*[text()="jq命令的使用"]')
        ActionChains(self.driver).scroll_to_element(ele).perform()
        time.sleep(5)