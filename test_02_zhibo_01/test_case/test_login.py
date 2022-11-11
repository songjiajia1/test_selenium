from time import sleep
import yaml
from selenium import webdriver


""""登录"""""
class TestCookieLogin():

    def setup_class(self):
        '''创建driver实例变量'''
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_class(self):
        # self.driver.quit()
        pass

    # 获取cookie
    def test_get_cookie(self):
        # 1.打开企业微信登录页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
        # 2.人工扫码登录
        sleep(10)
        # 3.获取cookie
        cook = self.driver.get_cookies()
        # 4.将获取到的cookie写入到文件中
        with open('../datas/cookie.yml', 'w') as f:
            yaml.safe_dump(cook, f)

    # 植入cookie
    def test_add_cookie(self):
        # 1.打开企业微信登录页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
        # 2.读取本地的cookies
        with open('../datas/cookie.yml') as f:
            cookie = yaml.safe_load(f)
        # 3.植入cookies
        for cook in cookie:
            self.driver.add_cookie(cook)
        # 4.再次访问企业微信
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
