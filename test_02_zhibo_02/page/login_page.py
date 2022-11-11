import yaml

from test_02_zhibo_02.page.base import Base
from test_02_zhibo_02.page.home_page import HomePage
from test_02_zhibo_02.utils.log_util import logger

"""登录页面"""
class LoginPage(Base):

    _BASE_URL_ = 'https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome'

    def login(self):
        # 登录
        logger.info('cookie登录')
        '''第二步：植入cookie完成登录'''
        # 1.打开企业微信登录页面
        # self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
        # 2.读取本地的cookies
        with open('../datas/cookie.yml') as f:
            cookie = yaml.safe_load(f)
        # 3.植入cookies
        for cook in cookie:
            self.driver.add_cookie(cook)
        # 4.再次访问企业微信
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')

        return HomePage(self.driver)