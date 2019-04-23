"""实现一段简单的中文编程"""
import time
import datetime
class Code:
    """自定义语言"""
    def __init__(self, text=None):
        self.text = text
class InterpreterBase:
    """自定义解释器基类"""
    def run(self, code):
        pass
class Interpreter(InterpreterBase):
    """实现解释器方法，实现终结符表达式字典"""
    def run(self, code):
        code = code.text
        code_dict = {'获取当前时间戳': time.time(), "获取当前日期": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        print(code_dict.get(code))
if __name__ == '__main__':
    test = Code()
    test.text = '获取当前时间戳'
    data1 = Interpreter().run(test)
    test.text = '获取当前日期'
    data2 = Interpreter().run(test)