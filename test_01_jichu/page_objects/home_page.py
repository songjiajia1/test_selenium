
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_01_jichu.page_objects.base_page import BasePage
from test_01_jichu.utils.log.log_util import logger
from test_01_jichu.utils.web_util import click_exception

'''首页'''
class HomePage(BasePage):

    __MENU_MALL_MANAGE = (By.XPATH, "//*[text()='商场管理']")
    __MENU_MALL_LEIMU = (By.XPATH, "//*[text()='商品类目']")

    """系统首页：进入商品类目"""
    def go_to_category(self):
        logger.info('系统首页：进入商品类目')
        # 点击“商场管理”，进入商品类目页面
        # self.do_find(self.__MENU_MALL_MANAGE).click()
        WebDriverWait(self.driver, 5).until(click_exception(*self.__MENU_MALL_MANAGE))
        # 点击“商品类目”
        self.do_find(self.__MENU_MALL_LEIMU).click()

        # ==》类目列表页面
        from test_01_jichu.page_objects.category_list_page import CategoryListPage
        return CategoryListPage(self.driver) # self.driver 是继承前一个步骤的浏览器，而不是重新打开一个浏览器