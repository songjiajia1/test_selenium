import logging
import os
from logging.handlers import RotatingFileHandler

__all__ = ['logger']

'''日志进阶
日志库采用模块化方法，并提供几类组件：
logers(记录器): 记录器提供应用程序代码直接使用的接口
Handlers(处理器): 处理器将日志记录（由记录器创建）发送到适当的目标
filters(过滤器): 过滤器提供了更细粒度的功能，用于确定要输出的日志记录
formatters(格式器): 格式器指定最终输出中日志记录的样式
'''

# 绑定句柄到logger对象
logger = logging.getLogger(__name__)
# 获取当前工具文件所在的路径
root_path = os.path.dirname(os.path.abspath(__file__))
# 拼接当前要打印的日志文件的路径
log_dir_path = os.sep.join([root_path, '..', f'/log'])
if not os.path.isdir(log_dir_path):
    os.mkdir(log_dir_path)
# 创建日志记录器，指明日志保存路径,每个日志的大小，保存日志的上限
file_log_handler = RotatingFileHandler(os.sep.join([log_dir_path, 'log.log']), maxBytes=1024 * 1024, backupCount=10, encoding='utf-8')
# 设置日志的格式
formatter = logging.Formatter(
    '[%(asctime)s] [%(filename)s]/[line: %(lineno)d]/[%(funcName)s] [%(levelname)s] %(message)s ')
# 日志输出到控制台的句柄
stream_handler = logging.StreamHandler()
# 将日志记录器指定日志的格式
stream_handler.setFormatter(formatter)
file_log_handler.setFormatter(formatter)
# 为全局的日志工具对象添加日志记录器
# 绑定句柄到logger对象
logger.addHandler(stream_handler)
logger.addHandler(file_log_handler)
# 设置日志输出级别
logger.setLevel(level=logging.DEBUG)

