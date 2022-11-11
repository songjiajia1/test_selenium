from time import sleep
import yaml
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from test_02_zhibo_01.utils.web_util import click_exception

""""登录"""""
class TestCookieLogin():

    def setup_class(self):
        '''第一步：创建一个driver实例变量'''
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        '''第二步：植入cookie完成登录'''
        # 1.打开企业微信登录页面
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')
        # 2.读取本地的cookies
        with open('../datas/cookie.yml') as f:
            cookie = yaml.safe_load(f)
        # 3.植入cookies
        for cook in cookie:
            self.driver.add_cookie(cook)
        # 4.再次访问企业微信
        # self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')

    def setup(self):
        # 执行每条用例的时候，都重新从首页开始
        self.driver.get('https://work.weixin.qq.com/wework_admin/loginpage_wx?from=myhome')

        # mock 测试数据，随机生成数据
        from faker import Faker
        fak = Faker('zh_CN') # 格式设置成中文
        self.name = fak.name() # 随机生成姓名
        self.phone_number = fak.phone_number() # 随机生成手机号
        self.accid = fak.ssn() # 随机生成账号

    def teardown_class(self):
        # self.driver.quit()
        pass


        '''添加通讯录成员'''
    def test_add_member(self):
        # 点击通讯录
        self.driver.find_element(By.ID, 'menu_contacts').click()
        # 点击添加成员
        aaa = (By.LINK_TEXT, '添加成员')
        WebDriverWait(self.driver, 5).until(click_exception(*aaa))
        # 输入姓名、账号、手机号
        self.driver.find_element(By.ID, 'username').send_keys(self.name)
        self.driver.find_element(By.ID, 'memberAdd_acctid').send_keys(self.accid)
        self.driver.find_element(By.ID, 'memberAdd_phone').send_keys(self.phone_number)
        # 点击保存
        self.driver.find_element(By.CSS_SELECTOR, '.js_btn_save').click()
        # 验证添加是否成功，断言toast的文本是不是’保存成功‘
        result = self.driver.find_element(By.ID, 'js_tips').text
        assert '保存成功' == result


    '''添加部门'''
    def test_add_part(self):
        part_name = '开发二部'

        # 点击通讯录
        self.driver.find_element(By.ID, 'menu_contacts').click()
        # 点击【+】按钮
        self.driver.find_element(By.CSS_SELECTOR, '.member_colLeft_top_addBtn').click()
        # 点击【添加部门】按钮
        self.driver.find_element(By.LINK_TEXT, '添加部门').click()
        # 输入部门名称
        self.driver.find_element(By.XPATH, '//input[@name="name"]').send_keys(part_name)
        # 点击所属部门
        self.driver.find_element(By.CSS_SELECTOR, '.js_parent_party_name').click()
        # 选择 交付部
        self.driver.find_element(By.XPATH, '//div[@class="inputDlg_item"]//a[text()="交付部"]').click()
        # 点击 确定
        # self.driver.find_element(By.XPATH, '//a[text()="确定"]')
        aaa = (By.XPATH, '//a[text()="确定"]')
        WebDriverWait(self.driver, 5).until(click_exception(*aaa))

        # 验证是否成功，断言toast的文本是不是’新建部门成功‘
        result = self.driver.find_element(By.ID, 'js_tips')
        assert '新建部门成功' == result.text

