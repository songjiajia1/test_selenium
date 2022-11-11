from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from test_02_zhibo_02.page.add_member_page import AddMemberPage
from test_02_zhibo_02.page.base import Base
from test_02_zhibo_02.utils.log_util import logger
from test_02_zhibo_02.utils.web_util import click_exception

"""首页"""
class HomePage(Base):

    def click_add_member(self):
        # 点击 添加成员 按钮
        logger.info('点击 添加成员 按钮')
        aaa = (By.LINK_TEXT, '添加成员')
        WebDriverWait(self.driver, 5).until(click_exception(*aaa))

        return AddMemberPage(self.driver)
