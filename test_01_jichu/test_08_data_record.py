import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from log.log_util import logger


class TestDataRecord:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def teardown_class(self):
        self.driver.quit()

    @pytest.mark.skip
    # 一、行为日志记录      作用：1.记录代码执行记录 方便复现；2。可以作为BUG依据
    def test_log_data_record(self):
        self.driver.get('https://www.sogou.com/')
        search_content = '霍格沃兹测试开发' # 把要搜索的内容定义成一个变量，方便调用
        # 搜索框输入搜索内容
        self.driver.find_element(By.ID, 'query').send_keys(search_content)
        logger.debug(f'搜索的内容是:{search_content}') # 记录debug级别的 日志 步骤
        self.driver.find_element(By.ID, 'stb').click()
        # 获取搜索结果（对应测试用例的实际结果）
        search_res = self.driver.find_element(By.CSS_SELECTOR, 'em') # 定位第一个 em 标签的元素，就是搜索到的实际结果
        logger.info(f'预期结果为：{search_content}, 实际结果为：{search_res.text}')
        # 断言 搜索内容与实际结果
        assert search_res.text == search_content



    # 二、步骤截图记录      作用：1.断言失败或成功截图；2.丰富测试报告；3.可以作为BUG依据
    def test_screenshot_record(self):
        self.driver.get('https://www.sogou.com/')
        search_content = '霍格沃兹测试开发'
        self.driver.find_element(By.ID, 'query').send_keys(search_content)
        logger.debug(f'搜索的内容是:{search_content}')
        self.driver.find_element(By.ID, 'stb').click()
        search_res = self.driver.find_element(By.CSS_SELECTOR, 'em') # 定位第一个 em 标签的元素，就是搜索到的实际结果
        logger.info(f'预期结果为：{search_content}, 实际结果为：{search_res.text}')
        # 截图记录
        self.driver.save_screenshot('search_res.png')
        assert search_res.text == search_content



    # 三、page_source(页面源代码)        作用：1.协助排查报错时元素当时是否存在页面上
    # 现象：出现了 no such element 的错误
    # 解决方案：在报错的代码行之前打印 page_source 确认定位的元素是否有问题
    def test_page_source_record(self):
        self.driver.get('https://www.sogou.com/')
        search_content = '霍格沃兹测试开发'
        # 把获取到的源码写到文件里
        with open('record.html', 'w', encoding='u8') as f:
            f.write(self.driver.page_source)
        self.driver.find_element(By.ID, 'query111').send_keys(search_content)
        # 获取page_source
        # logger.debug(self.driver.page_source)

