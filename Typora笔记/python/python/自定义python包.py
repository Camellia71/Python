#创建一个包
#导入自定义的包中的模块，并使用
from my_package.my_module1 import*
from my_package.my_module2 import*
info_print1()
info_print2()

#通过__all__变量，控制import*
#from my_package import*
#my_module1.info_print1()