#打开文件(open()函数)
f=open('test.txt','r',encoding=' UTF-8 ')
print(type(f))

#读取文件-read()
print(f.read())

#读取文件-readlines()返回一个列表将每一行放入每个元素
f.seek(0)
print(f.readlines())

#读取文件-readline()"每次读取一行"
f.seek(0)
print(f.readline())

#for循环读取文件()
f.seek(0)
for line in f:
    print(line)

#文件的关闭
f.close()

#with open 语法操作文件
with open('test.txt','r',encoding=' UTF-8 ') as f:
    for line in f:
        print(line)