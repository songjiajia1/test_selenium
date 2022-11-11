# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月10日
'''
from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestFuYong():

    # 浏览器复用，先手动扫码登录，拿到cookie
    def test_login(self):

        # 1.1 导入ChromeOptions()
        # opt = webdriver.ChromeOptions
        # 1.1 的第二种写法： 定义实例的配置对象
        opt = Options()
        # 2.修改实例属性为 就是debug的地址，并传给他，地址是复用的时候设置的 ip+端口
        opt.debugger_address='localhost:9222'
        sleep(2)
        # 3.实例化driver的时候，添加option 配置，这样就完成了复用
        driver = webdriver.Chrome(options=opt)
        driver.get('https://work.weixin.qq.com/wework_admin/frame')
        sleep(5)
        driver.find_element(By.XPATH, '.ww_indexImg_AddMember').click()
        driver.find_element(By.ID, 'username').send_keys('张三李四')
        # 4.拿到并打印cookie
        print(driver.get_cookies())
        cookie= driver.get_cookies()
        with open('cookie.yaml', 'w', encoding='UTF-8') as f:
            yaml.dump(cookie, f)

