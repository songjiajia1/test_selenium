

from selenium import webdriver

from test_02_zhibo_02.utils.log_util import logger

"""基类：实例化deiver、存放selenium API、封装各种方法"""
class Base:

    _BASE_URL_ = ''

    # 定义构造方法
    def __init__(self, base_driver=None):
        # 如果传入 base_driver 的话，就使用传入的 base_driver
        if base_driver:
            logger.info('这里是复用driver')
            self.driver = base_driver
        # 否则，如果不传的话，就重新启动一个driver
        else:
            logger.info('这里是创建一个新driver')
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)

        # 如果当前地址不是以http开头的，就导航到新地址中
        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL_)

    # 获取单个元素
    def do_find(self, by, value=None):
        logger.info(f'查找单个元素{by, value}')
        if value: # 如果传入的值不为空，就传入两个参数
            return self.driver.find_element(by, value)
        else: # 如果传入的值为空，就进行解元组操作
            return self.driver.find_element(*by)

    # 获取多个元素
    def do_finds(self, by, locator=None):
        logger.info(f'查找多个元素{by, locator}')
        if locator:
            return self.driver.find_elements(by, locator)
        else:
            return self.driver.find_elements(*by)

    # 输入文本
    def do_send_keys(self, value, by, locator=None):
        logger.info(f'输入内容的{value}')
        ele = self.do_find(by, locator)
        ele.clear()
        ele.send_keys(value)
