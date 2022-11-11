# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月06日
'''

from time import sleep
from selenium.webdriver.common.by import By
from Base.base import Base

# form 表单操作

class TestForm(Base):

    def test_form(self):
        self.driver.get('https://gitlab.stuq.ceshiren.com/users/sign_in')
        self.driver.find_element(By.ID, 'user_login').send_keys('sjiajia1994@163.com') # 输入用户名
        self.driver.find_element(By.ID, 'user_password').send_keys('songjiajia111') # 输入密码
        self.driver.find_element(By.ID, 'user_remember_me').click() # 勾选复选框
        self.driver.find_element(By.NAME, 'commit').click() # 点击登录按钮
        sleep(2)



