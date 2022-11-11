
from selenium.webdriver.common.by import By
from test_01_jichu.page_objects.base_page import BasePage
from test_01_jichu.utils.log.log_util import logger

'''登录页面'''
class LoginPage(BasePage):

    # 登录后台系统
    _BASE_URL_ = 'https://litemall.hogwarts.ceshiren.com/'

    __INPUT_USERNAME = (By.NAME, 'username')
    __INPUT_PASSWORD = (By.NAME, 'password')
    __BTN_LOGIN = (By.CSS_SELECTOR, '.el-button--primary')

    """登录页面：用户登录"""
    def login(self):
        # 访问登录页
        logger.info('登录页面：用户登录')
        # 输入“用户名”
        self.do_send_keys('manage', self.__INPUT_USERNAME)
        # 输入“密码”
        self.do_send_keys('manage123', self.__INPUT_PASSWORD)
        # 点击“登录”按钮
        self.do_find(self.__BTN_LOGIN).click()


        # ==》首页
        # ---这里导入的时候，要局部导入，只导入类方法，不要把整个类导过来---
        from test_01_jichu.page_objects.home_page import HomePage
        return HomePage(self.driver) # self.driver实例化后 继承前一个步骤的浏览器，传递到后续的页面中，共用一个浏览器
