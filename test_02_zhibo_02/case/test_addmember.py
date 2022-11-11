from test_02_zhibo_02.page.login_page import LoginPage


"""用例层，只关心业务，不关心怎么实现"""
class TestAddMember:

    def setup_class(self):
        self.home = LoginPage().login()

    def setup(self):
        # mock 测试数据，随机生成数据
        from faker import Faker
        fak = Faker('zh_CN') # 格式设置成中文
        self.name = fak.name() # 随机生成姓名
        self.phone_number = fak.phone_number() # 随机生成手机号
        self.accid = fak.ssn() # 随机生成账号

    def teardown_class(self):
        pass


    def test_add_member(self):
        """登录->首页->添加成员->输入信息->验证结果"""
        tips = self.home.click_add_member().fill_info(self.name, self.accid, self.phone_number).get_tips()
        assert '保存成功' == tips

