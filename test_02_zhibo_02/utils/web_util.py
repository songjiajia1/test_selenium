from test_01_jichu.utils.log.log_util import logger


"""工具类"""
def click_exception(by, element, max_attempts=5): # 最大点击次数
            def _inner(driver):
                # 多次点击按钮
                actul_attempts = 0 # 实际点击次数
                while actul_attempts<max_attempts:
                    actul_attempts += 1 # 每次循环，实际点击次数都要 + 1
                    try:
                        # 如果点击过程中报错，则直接执行 except Exception 这个逻辑，并且继续执行循环操作
                        driver.find_element(by, element).click()
                        # 如果点击成功，则直接return，并结束循环
                        return True
                    except Exception:
                        logger.debug('此次点击没有成功')
                # 当实际点击次数 大于 最大点击次数时，结束循环并抛出异常
                raise Exception('超出了最大点击次数')
            return _inner
