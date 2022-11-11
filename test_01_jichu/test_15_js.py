# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月08日
'''
from time import sleep
import pytest
from selenium.webdriver.common.by import By

from Base.base import Base

class TestJs(Base):

    # @pytest.mark.skip
    # 调用js来滑动页面
    def test_js_scroll(self):
        self.driver.get('https://www.sogou.com/')
        self.driver.find_element(By.ID, 'query').send_keys('selenium测试')
        # 通过 js 的方法来定位元素 定位 搜索 按钮   如果需要返回，可以加上return
        self.driver.execute_script('return document.getElementById("stb")').click()
        # 使用js的命令来滑动到页面底端
        self.driver.execute_script('document.documentElement.scrollTop=10000')
        sleep(2)
        self.driver.find_element(By.ID, 'sogou_next').click() # 点击下一页
        sleep(2)
        # 其他的一些 js 操作   并且返回出来值
        for code in [
                   # 网页的title               性能指标数据
            'return document.title', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
            # 也可以把方法合并在一起执行，效果基本一样
        print(self.driver.execute_script("return document.title; return JSON.stringify(performance.timing)"))


    # js处理-时间控件
    @pytest.mark.skip
    def test_datatime(self):
        self.driver.get('https://www.12306.cn/index/')
        # 找到 id 为train_date的时间控件，并返回出来一个元素
        self.driver.execute_script('a=document.getElementById("train_date")')
        # 去除日期控件的 readonly 属性
        self.driver.execute_script('a.removeAttribute("readonly")')
        # 为日期控件重新赋值，并返回出来，赋给data，也可以直接打印，都行
        data = self.driver.execute_script('return document.getElementById("train_date").value="2022-04-01"')
        print(f'出发时间是：{data}')
        sleep(3)


    #js处理只读的输入框，去除readonly属性，让输入框可以输入内容
    @pytest.mark.skip
    def test_readonly(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=tryjsref_password_readonly')
        # 找到id是 iframeResult 的iframe 元素，然后切换进去
        self.driver.switch_to.frame('iframeResult')
        # 先点击 设置只读 按钮，把输入框先设成只读格式
        self.driver.find_element_by_xpath('/html/body/button').click()
        # 找到frame下 id 为pwd的控件，并返回出来一个元素
        self.driver.execute_script('a=document.getElementById("pwd")')
        # 去除日期控件的 readonly 属性
        self.driver.execute_script('a.removeAttribute("readonly")')
        # 为控件重新赋值，并返回出来，赋给data，也可以直接打印，都行
        pawd = self.driver.execute_script('return document.getElementById("pwd").value="成功了666！"')
        print(f'输入的是密码是：{pawd}')
        sleep(2)

