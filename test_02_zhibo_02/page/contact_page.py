from selenium.webdriver.common.by import By
from test_02_zhibo_02.page.base import Base
from test_02_zhibo_02.utils.log_util import logger

"""通讯录页面"""
class Contact_Page(Base):

    _TEXT_TIPS = (By.ID, 'js_tips')

    def get_tips(self):
        # 获取添加成功的提示
        logger.info('获取添加成功的提示')
        result = self.do_find(self._TEXT_TIPS).text

        return result
