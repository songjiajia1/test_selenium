# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月08日
'''
from time import sleep
import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from Base.base import Base

class TestFile(Base):

    # 文件上传
    @pytest.mark.skip
    def test_file_upload(self):
        self.driver.get('https://image.baidu.com')
        self.driver.find_element(By.ID, 'sttb').click()
        self.driver.find_element(By.ID, 'uploadImg').send_keys('/Users/Administrator/Desktop/身份证照片/H-反面.jpg')
        sleep(3)


    # 弹框处理：案例
    # @pytest.mark.skip
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        # 切换到frame下
        self.driver.switch_to.frame('iframeResult')
        # 找到frame下的两个元素
        dra = self.driver.find_element(By.ID, 'draggable')
        dro = self.driver.find_element(By.ID, 'droppable')
        # 调用ActionChains方法
        action = ActionChains(self.driver)
        # 将元素1拖拽到元素2上
        action.drag_and_drop(dra, dro).perform()
        sleep(1)
        # 切换到alert中，并点击确定按钮
        print('点击alert的【确认】按钮')
        self.driver.switch_to.alert.accept()
        sleep(1)
        # 再切换回原来的frame，也就是默认的frame
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, 'submitBTN').click()
        sleep(1)
