import datetime as Date
today=Date.date.today().strftime('%Y-%m-%d')
now=Date.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('今日日期：',end='')
print(today)
print('当前时间：',end='')
print(now)