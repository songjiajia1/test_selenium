# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月08日
'''
from time import sleep
from selenium.webdriver.common.by import By
from Base.base import Base

# 自动登录虚拟机
class TestXuNi(Base):

    def test_xuni(self):
        self.driver.get('http://10.251.33.18/Citrix/storeWeb/')
        self.driver.find_element(By.XPATH, '//*[@id="protocolhandler-welcome"]/div/div/div/div/a').click()
        # 切换到alert中，并点击确定按钮
        self.driver.switch_to.alert.accept()
        sleep(2)

        self.driver.find_element(By.XPATH, '//*[@id="protocolhandler-detect"]/div/div/div/div/div[1]/a[3]').click()
        self.driver.find_element(By.ID, 'username').send_keys('kf0990')
        self.driver.find_element(By.ID, 'password').send_keys('admin!111')
        self.driver.find_element(By.ID, 'loginBtn').click()
        sleep(2)
        self.driver.find_element(By.ID, 'desktopsBtn').click()
        self.driver.find_element(By.XPATH, '/html/body/section[3]/div[2]/section[4]/div[4]/ul/li/a[2]').click()
        self.driver.find_element(By.ID, 'appInfoOpenBtn').click()
        sleep(3)



