'''给 test_14_browser.py 调用的'''
from _pytest.config import Config
from _pytest.config.argparsing import Parser


wen_env = {}
# 自定义 hook函数，实现命令行注册，解决自定义参数报错的问题
def pytest_addoption(parser:Parser):
    # 注册一个命令行组
    zuming = parser.getgroup('zuming')
    # 注册一个命令行参数
    # 第一个参数为指定的命令行的参数的形式
    # zuming.addoption('--browser', default='firefox', dest='browser', help='给命令行参数写注释')
    # default:设置默认浏览器
    # dest:给前边命令行指定的浏览器 起别名
    zuming.addoption('--browser')


def pytest_configure(config:Config):
    # browser = config.getoption('browser')
    browser = config.getoption('--browser')
    print(f'通过命令行获取到的浏览器为{browser}')
    wen_env['browser'] = browser