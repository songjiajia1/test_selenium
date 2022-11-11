# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月01日
'''
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestHW:
    def setup(self):
        # 初始化 driver，加self实例化
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3) # 隐式等待

    def teardown(self):
        self.driver.quit() # 关闭浏览器

    # @pytest.mark.skip
    def test_baidu(self):
        self.driver.get('https://www.sogou.com/')
        # self.driver.find_element(By.ID, 'kw').send_keys('霍格沃兹测试学院')
        # self.driver.find_element(By.XPATH, '//*[@id="kw"]').send_keys('霍格沃兹测试学院')
        self.driver.find_element(By.CSS_SELECTOR, '#query').send_keys('霍格沃兹测试开发')
        self.driver.find_element(By.ID, 'stb').click()
        # self.driver.find_element(By.XPATH, '//*[@id="2"]/h3/a').click()
        # 用js滑动到底部，找到id为 sogou_next 的元素，点击
        self.driver.execute_script('document.documentElement.scrollTop=20000')
        self.driver.find_element(By.ID, 'sogou_next').click()
        result = self.driver.find_element(By.CSS_SELECTOR, '#sogou_prev')
        # 获取到定位的文本信息
        # 判断实际获取到的信息和预期值是否一致
        assert result.text == '上一页'
        logging.info('断言成功')
        # 刷新浏览器
        self.driver.refresh()
        # 返回上一页
        self.driver.back()
        # 最小化浏览器
        self.driver.minimize_window()