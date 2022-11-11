
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_01_jichu.page_objects.base_page import BasePage
from test_01_jichu.utils.log.log_util import logger

'''列表页面'''
class CategoryListPage(BasePage):

    __BTN_ADD = (By.XPATH, "//*[text()='添加']")
    __MSG_ADD_OPERATE = (By.XPATH, "//*[(text()='创建成功')]")
    __MSG_DELETE_OPERATE = (By.XPATH, "//*[(text()='删除成功')]")

    """类目列表页面：点击添加"""
    def click_add(self):
        logger.info('类目列表页面：点击添加')
        # 点击“添加”按钮
        self.do_find(self.__BTN_ADD).click()
        # ==》创建类目页面
        from test_01_jichu.page_objects.category_create_page import CategoryCreatePage
        return CategoryCreatePage(self.driver) # self.driver 是继承前一个步骤的浏览器，而不是重新打开一个浏览器


    """类目列表页面：获取‘创建成功’的操作结果"""
    def get_operate_result(self):
        logger.info('类目列表页面：获取‘创建成功’的操作结果')
        # 获取冒泡消息文本
        ele = self.wait_element_until_visible(self.__MSG_ADD_OPERATE) # 里边需要传一个元组
        # 消息文本
        msg = ele.text
        logger.info(f'冒泡消息是：{msg}')
        # ==》返回消息文本
        return msg


    '''定义一个删除的方法'''
    def delete_category(self, category_name):
        logger.info('类目列表页面：获取’删除操作‘')
        # 找到指定的类目，点击删除按钮，进行删除
        self.do_find(By.XPATH, f"//*[text()='{category_name}']/../..//*[text()='删除']").click()
        # ==》跳转到当前页
        return CategoryListPage(self.driver)


    """类目列表页面：获取‘删除成功’的操作结果"""
    def get_delete_result(self):
        logger.info('类目列表页面：获取‘删除成功’的操作结果')
        # 获取冒泡消息文本
        ele = self.wait_element_until_visible(self.__MSG_DELETE_OPERATE) # 里边需要传一个元组
        # 消息文本
        msg = ele.text
        logger.info(f'冒泡消息是：{msg}')
        # ==》返回消息文本
        return msg