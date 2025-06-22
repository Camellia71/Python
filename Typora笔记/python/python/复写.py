class Phone:
    IMET=None
    producer="ITCAST"

    def call_by_5g(self):
        print("使用5g网络进行通信")

#定义子类，复写父类成员
class MyPhone(Phone):
    producer="IT"

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话时省电")
        print("使用5g网络进行通话")
        print("关闭CPU单核模式，确保性能")
        print(f"{super().producer}")
        super().call_by_5g()

phone=MyPhone()
phone.call_by_5g()
print(phone.producer)