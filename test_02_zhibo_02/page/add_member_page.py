from selenium.webdriver.common.by import By
from test_02_zhibo_02.page.base import Base
from test_02_zhibo_02.page.contact_page import Contact_Page
from test_02_zhibo_02.utils.log_util import logger

"""添加成员页面"""
class AddMemberPage(Base):

    _INPUT_NAME = (By.ID, 'username')
    _INPUT_ACCID = (By.ID, 'memberAdd_acctid')
    _INPUT_PHONE = (By.ID, 'memberAdd_phone')
    _BTN_SAVE = (By.CSS_SELECTOR, '.js_btn_save')

    def fill_info(self, name, accid, phone_number):
        # 输入用户名、账号、手机号
        logger.info('输入内容')
        self.do_send_keys(name, self._INPUT_NAME)
        self.do_send_keys(accid, self._INPUT_ACCID)
        self.do_send_keys(phone_number, self._INPUT_PHONE)
        # 点击保存
        self.do_find(self._BTN_SAVE).click()

        return Contact_Page(self.driver)