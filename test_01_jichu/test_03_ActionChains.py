# -*- coding: utf-8 -*-
'''
/usr/bin/env python
时间：2021年12月05日
'''
import sys
from time import sleep
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from Base.base import Base


# ActionChains 用法

class TestActionChains(Base):

    # https://sahitest.com/demo/clicks.htm 测试例子 链接
    # https://vip.ceshiren.com/#/ui_study/frame
    # https://sahitest.com/demo/dragDropMooTools.htm

    # 点击、右键、双击操作
    @pytest.mark.skip # 如果不执行这条用例，就用这个标签
    def test_case_click(self):
        self.driver.get("https://sahitest.com/demo/clicks.htm")
        # element_clcik = self.deiver.find_element_by_xpath('/html/body/form/input[3]') # 和下边这行一样，写法不同而已
        element_click = self.driver.find_element(By.XPATH, '//input[@value="click me"]') # 点击
        element_doubleclick = self.driver.find_element(By.XPATH, '//input[@value="dbl click me"]') # 双击
        element_rightclick = self.driver.find_element(By.XPATH, '//input[@value="right click me"]') # 右键
        element_clear = self.driver.find_element(By.XPATH, '//input[@value="Clear"]') # 清空
        action = ActionChains(self.driver)
        action.double_click(element_doubleclick).pause(1) # 双击
        action.click(element_click).pause(1) # 左键单击
        action.click(element_clear).pause(1) # 清空
        action.context_click(element_rightclick) # 右键
        action.perform() # 需要调用perform这个方法,才能执行上边的方法
        sleep(2)

    # 鼠标 左键 双击
    @pytest.mark.skip
    def test_double(self):
        self.driver.get('https://vip.ceshiren.com/#/ui_study')
        ele = self.driver.find_element(By.ID, 'primary_btn')
        ActionChains(self.driver).double_click(ele).pause(2).perform()


    # 鼠标移动到某个元素上   move_to_element  # 这个是鼠标悬停方法
    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get('https://www.baidu.com/')
        ele = self.driver.find_element(By.LINK_TEXT, '更多')
        # ele = self.driver.find_element_by_name("tj_briicon")
        elem = self.driver.find_element(By.ID, 's-usersetting-top')
        eell = self.driver.find_element(By.XPATH, '//*[@id="s_qrcode_nologin"]//img[1]')
        action = ActionChains(self.driver)
        action.move_to_element(ele).pause(2) # 鼠标在“更多”元素上悬停2秒
        action.move_to_element(elem).pause(2) # 鼠标在“设置”元素上悬停2秒
        action.move_to_element(eell).pause(2) # 鼠标在“二维码”元素上悬停2秒
        action.perform()

    @pytest.mark.skip
    # 1.鼠标悬停到元素上
    def test_move_to_element(self):
        self.driver.get('https://vip.ceshiren.com/#/ui_study/action_chains2')
        ele = self.driver.find_element(By.CSS_SELECTOR, '.title')
        ActionChains(self.driver).move_to_element(ele).pause(2).perform()
    # 2.点击下拉框中的枚举值
        self.driver.find_element(By.XPATH, '//*[text()=" 测开班 "]').click()


    # 将一个元素拖拽到某个元素上   drag_and_drop
    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get('https://sahitest.com/demo/dragDropMooTools.htm')
        drag_element = self.driver.find_element(By.ID, 'dragger') # 第一个元素
        drop_element = self.driver.find_element(By.XPATH, '/html/body/div[2]') # 第二个元素
        action = ActionChains(self.driver) # 创建ActionChains实例化
        # 将第一个元素拖到第二个元素上用 drag_and_drop 这个方法
        action.drag_and_drop(drag_element, drop_element).perform() # 第一种写法
        # action.click_and_hold(drag_element).release(drop_element).perform() # 第二种写法
        # action.click_and_hold(drag_element).move_to_element(drop_element).release().perform() # 第三种写法
        #        点击并且按住不放                滚动到第二个元素上                再释放
        sleep(2)

    @pytest.mark.skip
    def test_drag_and_drop(self):
        self.driver.get('https://vip.ceshiren.com/#/ui_study/action_chains')
        # 点击  起始元素
        ele = self.driver.find_element(By.ID, 'item1')
        # 拖动到  目标元素
        sss = self.driver.find_element(By.ID, 'item3')
        ActionChains(self.driver).drag_and_drop(ele, sss).pause(1).perform()
        # 点击 重置 按钮
        self.driver.find_element(By.ID, 'reset').click()
        sleep(2)


    # ActionChains 方法 模拟键盘按键
    @pytest.mark.skip
    def test_keys(self):
        self.driver.get('https://sahitest.com/demo/label.htm')
        ele = self.driver.find_element(By.XPATH, '/html/body/label[1]/input')
        ele.click() # 需要先把光标放在元素上，所以这里点击一下
        action = ActionChains(self.driver)
        # send_keys 需要传入一个 keys_to_send 这样一个参数，这个参数是发给键盘的一些指令，调用的是 keys 这个模块
        # 括号中是 keys 可以模拟键盘的各种操作
        action.send_keys('name:').pause(1) # 输入字符   pause 是等待的意思
        action.send_keys(Keys.SPACE).pause(1) # 调用空格键
        action.send_keys('Tom').pause(1) # 输入字符
        action.send_keys(Keys.SEMICOLON) # 输入分号
        action.send_keys(Keys.BACK_SPACE) # 回退一步
        action.perform()
        sleep(2)


    @pytest.mark.skip
    def test_a(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element(By.CSS_SELECTOR, '#kw').click()
        action = ActionChains(self.driver)
        action.send_keys('selenium').pause(1).perform()
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.CONTROL, 'a')  # 全选
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys(Keys.CONTROL, 'x')  # 剪切
        sleep(2)
        self.driver.get('http://www.sogou.com')
        self.driver.find_element(By.CSS_SELECTOR, '.sec-input').send_keys(Keys.CONTROL, 'v')  # 粘贴
        sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, '#stb').click()
        sleep(2)
        self.driver.quit()

    @pytest.mark.skip
    def test_aa(self):
        self.driver.get('https://www.sogou.com/')
        action = ActionChains(self.driver)
        # 输入框输入内容
        self.driver.find_element(By.ID, 'query').click()
        action.send_keys('seleniumm').pause(1)
        # 删除多输入的一个 m
        action.send_keys(Keys.BACK_SPACE).pause(1)
        # 输入空格键+“教程”
        action.send_keys(Keys.SPACE).pause(1)
        action.send_keys('教程').pause(1)
        # ctrl+a 全选输入框内容
        action.key_down(Keys.CONTROL).key_up('a').pause(1)
        # ctrl+x 剪切输入框内容
        action.key_down(Keys.CONTROL).key_up('x').pause(1)
        # ctrl+v 粘贴内容到输入框
        action.key_down(Keys.CONTROL).key_up('v').pause(1)
        # 通过回车键盘来代替点击操作
        action.key_down(Keys.ENTER).pause(1)
        # 回退键 ESC
        action.key_down(Keys.ESCAPE).pause(1)

        # action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).pause(1)
        # action.key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).pause(1)
        # action.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).pause(1)
        # su = self.driver.find_element_by_id('su')
        # action.click(su).pause(3)
        action.perform()

    # 复制粘贴
    @pytest.mark.skip
    def test_command_control(self):
        self.driver.get('https://ceshiren.com/')
        self.driver.find_element(By.ID, 'search-button').click() # 点击搜索按钮
        ele = self.driver.find_element(By.ID, 'search-term')
        # 判断操作系统是否为 mac 如果是则返回 command 键位，如果是Windows 则返回 control 键位
        command_control = Keys.COMMAND if sys.platform == 'darwin' else Keys.CONTROL
        # 1.按住shift键 输入内容 2.按住键盘 左键 并选中内容
        # 3.按住 control+x 再粘贴 vvv 相当于粘贴3次
        # 4.松开键盘
        ActionChains(self.driver)\
            .key_down(Keys.SHIFT, ele).send_keys('selenium#')\
            .key_down(Keys.ARROW_LEFT)\
            .key_down(command_control).send_keys('xvvv')\
            .key_up(command_control).pause(2).perform()


    # 点击搜索按钮，搜索框输入内容的同时，按下shift键，实现输入的内容变成大写
    @pytest.mark.skip
    def test_shift(self):
        self.driver.get('https://ceshiren.com/')
        self.driver.find_element(By.ID, 'search-button').click() # 点击搜索按钮
        ele = self.driver.find_element(By.ID, 'search-term')
        # key_down()表示按下某个键，send_keys()表示输入内容
        ActionChains(self.driver).key_down(Keys.SHIFT, ele).send_keys('selenium').perform()


# 调用pytest 来执行这个方法
if __name__ == '__main__':
    pytest.main(['-vs','test_03_ActionChains.py'])  # 需要告诉它要执行哪个类


