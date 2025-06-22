f=open('test.txt','r',encoding='UTF-8')
for line in f:
    print(line.strip('\n').strip('；').split('，'))