#导入自定义模块使用
from my_module1 import*
test_a(1,2)

#导入不同模块的同名功能
from my_module1 import*
from my_module2 import*
test(1,2)

#__main__变量
"""函数内部测试点"""

#__all__变量
"""__all__只会作用于'*'上，可以正常使用from import 语句"""

from my_module1 import*
test_a(1,2)
test_b(1,2)