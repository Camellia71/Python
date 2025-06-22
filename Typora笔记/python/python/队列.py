class Queue:
    def __init__(self,size):
        self.size=size           #队列大小
        self.queue=[0]*self.size #创建队列
        self.front=0             #队首
        self.rear=0              #队尾
    #进队
    def push(self,element):
        if not self.is_full():
           self.rear=(self.rear+1)%self.size
           self.queue[self.rear]=element
        else:
            raise IndexError("Queue is filled")
    #出队
    def pop(self):
        if not self.is_empty():
            self.front=(self.front+1)%self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty")
    #判断队空
    def is_empty(self):
        if self.rear == self.front:
            return True
    #判断队满
    def is_full(self):
        if (self.rear+1)%self.size == self.front:
            return True

q=Queue(11)
for i in range(1,11):
    q.push(i)
print(q.queue)