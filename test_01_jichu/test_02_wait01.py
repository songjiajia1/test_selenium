from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# 隐式等待
# def test_wait_1():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get('https://vip.ceshiren.com/')
#     driver.implicitly_wait(3)
#     driver.find_element(By.XPATH, '//*[text()="个人中心"]')

# 显示等待 解决元素不能点击的问题
# def test_wait_2():
#     driver = webdriver.Chrome()
#     driver.maximize_window()
#     driver.get('https://vip.ceshiren.com/#/ui_study')
#     WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable((By.ID, 'success_btn')))
#     driver.find_element(By.ID, 'success_btn').click()
#     sleep(2)


# 输入1：要点击的目标按钮，输入2：下一个页面的某个元素
def my_to_be_clickable(target_element, next_element):
    def _inner(driver):
        # 点击目标按钮
        driver.find_element(*target_element).click()
        '''如果找到下一个页面的元素，return出去的内容就为 webelement 对象
        如果没有找到，那么 driver.find_element(*next_element) 这行代码就报错
        但是会被 until 中的异常捕获逻辑捕获异常，循环会继续执行，直到规定的时间循环结束'''
        return driver.find_element(*next_element)
    return _inner


''' 问题：使用官方提供的 expected condition，已经无法满足需求，有些按钮需要点击多次才可以
    解决方法：自己封装期望条件，一直点击按钮，直到下一个页面的元素出现为止
'''
def test_wait_3():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://vip.ceshiren.com/#/ui_study')
    WebDriverWait(driver, 5000).until(
        my_to_be_clickable((By.ID, 'primary_btn'),(By.XPATH, '//*[text()="该弹框点击两次后才会弹出"]')))
    sleep(2)
