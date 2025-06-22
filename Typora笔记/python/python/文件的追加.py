#整体与文件的写入一样
#打开不存在的文件时直接写入，若文件存在则直接追加
f=open('test1.txt','a',encoding='UTF-8')
f.write('\nhello world')
