# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月07日
'''
import os
from selenium import webdriver


# 多浏览器兼容性测试
class Base():
    def setup(self):
        # 通过下边这行来获取传过来的参数
        browser = os.getenv('browser')
        # 判断传进来的参数是什么，然后就打开相应的浏览器
        if browser == 'firefox':
            self.driver = webdriver.Firefox()
        elif browser == 'ie':
            self.driver = webdriver.Ie()
        elif browser == 'headless':
            self.driver = webdriver.PhantomJS()
        else:
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()

