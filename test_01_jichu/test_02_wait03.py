# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月22日
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait():
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://ceshiren.com/latest')
        self.driver.implicitly_wait(3)

    def teardown(self):
        self.driver.quit()

    def test_wait(self):
        # 1.点击 所有分类
        self.driver.find_element(By.XPATH, '//*[@title="所有分类"]').click()
        # 2.判断 所有分类下的“最新”字段出现没有
        # def wait(a):
        #     return len(self.driver.find_elements_by_xpath('//*[@class="table-heading"]')) >= 1
        # WebDriverWait(self.driver, 5).until(wait)
        # 确定返回值是否为 webelement 对象要点进condition中的源码进行查看，不是所有的expected_conditions 的返回值都是webelement对象
        WebDriverWait(self.driver, 5).until(expected_conditions.element_to_be_clickable((By.XPATH, '//*[@class="table-heading"]')))
        # 3.如果 所有分类下的“最新”字段出现了，就点击 最新 菜单
        self.driver.find_element(By.XPATH, '//*[@title="有新帖子的话题"]').click()
