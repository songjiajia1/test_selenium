"""公共父类"""
import time
import allure
from selenium import webdriver

# 基类
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    _BASE_URL_ = ''

    # 定义构造方法
    def __init__(self, base_driver=None):
        # 如果传入 base_driver 的话，就使用传入的 base_driver
        if base_driver:
            self.driver = base_driver
        # 否则，如果不传的话，就新启动一个driver
        else:
            self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(3)

        # 如果当前地址不是以http开头的，就导航到新地址中
        if not self.driver.current_url.startswith("http"):
            self.driver.get(self._BASE_URL_)

    def do_find(self, by, locator=None):
        # 想要获取单个元素
        if locator:
            # 如果传入两个参数，那么就传两个参数到 find_element 中
            return self.driver.find_element(by, locator)
        else:
            # 如果传入的是一个元组或者其他对象，就进行解包，来获取单个的元素
            return self.driver.find_element(*by)

    def do_finds(self, by, locator=None):
        # 想要获取多个元素
        if locator:
            # 如果传入两个参数，那么就传两个参数到 find_element 中
            return self.driver.find_elements(by, locator)
        else:
            # 如果传入的是一个元组或者其他对象，就进行解包，来获取多个的元素
            return self.driver.find_elements(*by)

    # 适用于清空输入框的内容，输入什么值、定位策略、定位方式
    def do_send_keys(self, value, by, locator=None):
        ele = self.do_find(by, locator) # 先获取整个输入框
        ele.clear() # 再清空
        ele.send_keys(value) # 再输入值就行了

    def do_quit(self):
        self.driver.quit()

    # 获取截图
    def get_screenshot(self):
        timestamp = int(time.time())
        # 要提前创建好 images 路径
        image_path = f'../images/image_{timestamp}.PNG'
        # 截图
        self.driver.save_screenshot(image_path)
        # 将截图放到测试报告中    文件路径    名称                          格式
        allure.attach.file(image_path, name='picture', attachment_type=allure.attachment_type.PNG)

    # 定义一个显示等待，进行链式调用
    def wait_element_until_visible(self, locator:tuple):
        return WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))