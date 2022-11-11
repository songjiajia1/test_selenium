# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月12日
'''
from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# 通过Cookie或者Remote浏览器复用完成添加联系人测试用例
def test_add_contacts():
    # 复用浏览器，获取cookie
    option = webdriver.ChromeOptions()
    option.debugger_address='127.0.0.1:9222'
    driver = webdriver.Chrome(options=option)
    # 设置全局的隐式等待
    driver.implicitly_wait(10)
    # 进入首页
    driver.get('https://work.weixin.qq.com/wework_admin/frame#index')
    # 点击通讯录
    driver.find_element(By.ID, 'menu_contacts').click()
    # 设置一个显示等待，等待 直到'添加成员'这个元素可被点击
    ele = (By.CSS_SELECTOR, 'div:nth-child(1) > a.qui_btn.ww_btn.js_add_member')
    WebDriverWait(driver, 3).until(expected_conditions.element_to_be_clickable(ele))
    # 点击 添加成员 按钮，进入信息填写页面
    driver.find_element(By.CSS_SELECTOR, 'div:nth-child(1) > a.qui_btn.ww_btn.js_add_member').click()
    # 填写信息
    driver.find_element(By.ID, 'username').send_keys('张三') # 姓名
    driver.find_element(By.ID, 'memberAdd_acctid').send_keys('112233') # 账号
    driver.find_element(By.ID, 'memberAdd_phone').send_keys('13300002222') # 手机号
    driver.find_element(By.CSS_SELECTOR, '.qui_btn.ww_btn.js_btn_save').click() # 点击保存
    sleep(2)
    # 断言是否添加成功
    

