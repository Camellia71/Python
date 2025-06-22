#继承语法：
"""
class 类名（父类名，父类，父类......）：
      内容体（pass）
"""

#演示单继承
class Phone:
    IMEI=None         #序列号
    producer="HM"     #厂商

    def call_by_4g(self):
        print("4g通话")

class Phone2025(Phone):
    face_id="10001"

    def call_by_5g(self):
        print("2025年新功能：5通话")

phone=Phone2025()
print(phone.producer)
phone.call_by_4g()
phone.call_by_5g()