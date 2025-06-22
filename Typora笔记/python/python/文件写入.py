#打开文件，不存在的文件
f1=open('test1.txt','w',encoding='UTF-8')

#write写入
f1.write("hello world!!!")

#flush刷新
f1.flush()

#close关闭(close函数内置flush函数)
f1.close()

#打开一个存在的文件
f=open('test1.txt','w',encoding='UTF-8')

#write写入flush刷新
f.write('yu jia cheng')

#close关闭
f.close()