"""私有成员变量和方法不能被类对象访问，只能在类内部进行访问"""
class Phone:

    __current_voltage=None

    def __keep_single_core(self):
        print("让CPU以单核模式运行")

phone=Phone()
#phone.__keep_single_core()
print(phone.__cerrent_voltage)