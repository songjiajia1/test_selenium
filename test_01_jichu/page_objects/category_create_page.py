
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from test_01_jichu.page_objects.base_page import BasePage
from test_01_jichu.utils.log.log_util import logger
from test_01_jichu.utils.web_util import click_exception

'''创建类目页面'''
class CategoryCreatePage(BasePage):

    __INPUT_LEIMU_NAME = (By.CSS_SELECTOR, ".el-input__inner")
    __BTN_JIBIE = (By.CSS_SELECTOR, ".el-icon-arrow-up")
    __BTN_YIJILEIMU = (By.XPATH, "//body/div[3]//li[1]/span")
    __BTN_QUEDING = (By.XPATH, "//*[text()='确定']")

    """创建类目页面：创建类目"""
    def create_category(self, category_name):
        logger.info('创建类目页面：创建类目')

        # 输入“类目名称”
        self.do_send_keys(category_name, self.__INPUT_LEIMU_NAME)
        # 点击’级别‘下拉框，点击’一级类目‘枚举值
        self.do_find(self.__BTN_JIBIE).click()
        # self.do_find(self.__BTN_YIJILEIMU).click()
        WebDriverWait(self.driver, 5).until(click_exception(*self.__BTN_YIJILEIMU))

        # 点击“确定”按钮
        WebDriverWait(self.driver, 5).until(click_exception(*self.__BTN_QUEDING)) # * 是解包操作

        # ==》类目列表页面
        from test_01_jichu.page_objects.category_list_page import CategoryListPage
        return CategoryListPage(self.driver) # self.driver 是继承前一个步骤的浏览器，而不是重新打开一个浏览器