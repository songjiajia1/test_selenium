from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestCookieLogin():

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    # 打开新的浏览器，传递给selenium，设置cookie，跳过扫码登录
    def test_get_cookies(self):
        # 1.打开扫码登录的页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
        # 2.等待几秒，进行人工扫码
        sleep(10)
        # 3.成功登录后，再去获取cookie信息
        cookies = self.driver.get_cookies()
        # 4.将获取到的cookie存入到可持久存储的地方，文件或者数据库中
        with open('cookies.yml', 'w') as f:
            yaml.safe_dump(cookies, f)

    def test_add_cookie(self):
        # 1.打开扫码登录的页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
        # 2.定义cookie，cookie信息从之前写入的文件中获取
        cookies = yaml.safe_load(open('cookies.yml'))
        # 3.循环遍历cookie，植入cookie
        for coo in cookies:
            self.driver.add_cookie(coo)
        # 4.用cookie登录后，去点击页面的元素
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#customer/analysis')
        sleep(1)
