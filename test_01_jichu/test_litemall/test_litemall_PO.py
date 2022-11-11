import allure
import sys
import pytest

from test_01_jichu.page_objects.login_page import LoginPage
sys.path.append("../..")

class TestLitemall:

    def setup_class(self):
        """登录页面：用户登录"""
        self.home = LoginPage().login()

    def teardown_class(self):
        self.home.do_quit()


    @allure.story('新增功能')
    @pytest.mark.parametrize("caregory_name", ['aaa', 'bbb', 'ccc'])
    def test_new(self, caregory_name):
        list_page = self.home\
            .go_to_category()\
            .click_add()\
            .create_category(caregory_name)

        # 断言结果
        res = list_page.get_operate_result()
        assert '创建成功' == res

        # 数据清理
        list_page.delete_category(caregory_name)


    @allure.story('删除功能')
    @pytest.mark.parametrize("caregory_name", ['delaaa', 'delbbb', 'delccc'])
    def test_delete(self,caregory_name):
        res = self.home\
            .go_to_category()\
            .click_add()\
            .create_category(caregory_name)\
            .delete_category(caregory_name)\
            .get_delete_result()
        assert '删除成功' == res
