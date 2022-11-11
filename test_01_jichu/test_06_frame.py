# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月07日
'''
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Base.base import Base
from time import sleep

class TestFrame(Base):

    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 找到id是 iframeResult 的iframe 元素，然后切换进去
        self.driver.switch_to.frame('iframeResult') # 切换frame
        # self.driver.switch_to_frame('iframeResult') # 和上一行一样
        # 找到frame下 id是 draggable 和 droppable 的frame 元素
        a1 = self.driver.find_element(By.ID, 'draggable') # 第一个元素
        a2 = self.driver.find_element(By.ID, 'droppable') # 第二个元素
        action = ActionChains(self.driver)
        action.drag_and_drop(a1,a2).perform() # 将第一个元素拖拽到第二个元素上
        sleep(2)
        self.driver.switch_to.alert.accept() # 切换到alert中，并点击确定按钮
        sleep(2)
        self.driver.switch_to.parent_frame() # 再切换到父级frame
        # self.driver.swith_to.default.content() # 这个是切换到默认的frame
        self.driver.find_element(By.ID, 'submitBTN').click() # 再对当前页面的元素进行操作
        sleep(1)

