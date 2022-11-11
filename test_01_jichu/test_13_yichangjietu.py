import time
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By

'''实现代码异常的时候，截图/打印 page_source
实现方法：try catch 配合截图/ page_source操作
问题1：异常处理会影响用例本身的执行结果
---解决方案：在expected 之后用 expected Exception 再把异常抛出
问题2：异常捕获处理代码和业务代码无关，不能耦合
---解决方案：使用装饰器装饰用例或者相关方法，这样就不会体现在用例种了
问题3：需要通过driver实例截图/打印page_source，需要装饰器先去获取driver对象
---解决方案：
'''

# 自定义一个装饰器
def ui_exception_record(func1):
    def _inner(*args, **kwargs):
        try:
            # 当被装饰的函数/方法发生异常，就捕获并记录
            func1(*args, **kwargs)
        except Exception:
            # 获取被装饰方法的self，也就是实例对象
            '''通过self 就可以拿到声明的实例变量driver
            但前提条件是，1、被装饰的方法是一个实例方法；2、实例需要有实例变量，也就是self.driver。说的是下边的那个方法：test_baidu()'''
            driver = args[0].driver
            # 上边出现异常，就执行这里边的代码
            print('上边出现异常了！！')
            # 截图操作
            timestamp = int(time.time())
            image_path = f'./images/image_{timestamp}.PNG'
            page_source_path = f'./page_source/page_source_{timestamp}.html'
            # 截图
            driver.save_screenshot(image_path)
            # 记录 page_source
            with open(page_source_path, 'w', encoding='u8') as f:
                f.write(driver.page_source)
            # 将截图 放在报告中
            allure.attach.file(image_path, name='picture', attachment_type=allure.attachment_type.PNG)
            # 将page_source 记录到报告中
            # 1、如果在报告中想要页面格式的，就用html格式写
            # allure.attach.file(page_source_path, name='page_source', attachment_type=allure.attachment_type.HTML)
            # 2、如果在报告中想要源码格式的，就用text格式写
            allure.attach.file(page_source_path, name='page_source', attachment_type=allure.attachment_type.TEXT)
            raise Exception
    return _inner

class TestBaidu:

    @ui_exception_record
    def test_baidu(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://baidu.com/')
        # 如果发生异常，例如：元素找不到
        self.driver.find_element(By.ID, 'su1')

        self.driver.quit()
