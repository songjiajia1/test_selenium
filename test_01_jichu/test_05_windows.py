# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月07日
'''

from time import sleep
from selenium.webdriver.common.by import By
from Base.base import Base

# 窗口之间来回切换操作

class TestWindows(Base): # 继承 Base类中的 setup 和 teardown

    def test_windows(self):
        self.driver.get('https://www.baidu.com/')
        self.driver.find_element(By.LINK_TEXT, '登录').click() # 找到登录
        self.driver.find_element(By.LINK_TEXT, '立即注册').click() # 点击立即注册
        print(self.driver.current_window_handle) # ------------------------------------------当前窗口
        print(self.driver.window_handles) # -------------------------------------------------所有窗口
        window = self.driver.window_handles # 这个是注册窗口
        # 切换到最后一个窗口，也就是注册窗口，因为上边这行找到的是一个列表，所以取最后一个
        self.driver.switch_to.window(window[-1])
        print(self.driver.current_window_handle) # ------------------------------------------当前窗口
        self.driver.find_element(By.XPATH, '//*[@id="TANGRAM__PSP_4__userName"]').send_keys('usersongjj')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__phone').send_keys('19800001001')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_4__password').send_keys('123qweasd!')
        self.driver.find_element(By.ID, 'login_btn').click() # 点击上边的 登录 按钮
        sleep(2)

        # 切换到扫码登录弹框 ------ 不用切换了，因为没有打开新窗口
        # window_1 = self.driver.window_handles
        # self.driver.switch_to.window(window_1[-1])

        # 扫码登录弹框中 点击用户名登录，进行操作
        print(self.driver.current_window_handle) # ------------------------------------------当前窗口
        self.driver.find_element(By.ID, 'TANGRAM__PSP_31__footerULoginBtn').click()
        self.driver.find_element(By.ID, 'TANGRAM__PSP_31__userName').send_keys('usersongjj')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_31__password').send_keys('19800001001')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_31__submit').click()
        sleep(2)

        # 切换回第一个页面（window[0]），进行账号登录
        self.driver.switch_to.window(window[0])
        print(self.driver.current_window_handle) # ------------------------------------------当前窗口
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__userName').send_keys('usersongjj')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__password').send_keys('19800001001')
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__submit').click()
        sleep(2)

        # 点击忘记密码，切换到找回密码页面
        self.driver.find_element(By.ID, 'TANGRAM__PSP_11__fgtpwdLink').click()
        window_2 = self.driver.window_handles
        self.driver.switch_to.window(window_2[-1])
        print(self.driver.current_window_handle) # ------------------------------------------当前窗口
        print(self.driver.window_handles) # -------------------------------------------------所有窗口
        self.driver.find_element(By.ID, 'account').send_keys('19800002001')
        self.driver.find_element(By.ID, 'submit').click()
        sleep(2)

