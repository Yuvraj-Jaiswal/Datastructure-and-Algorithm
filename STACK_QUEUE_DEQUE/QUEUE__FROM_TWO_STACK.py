
class QUEUE_from_stack():

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def low(self):
        return self.stack2[len(self.stack2)-1]

    def add_que(self,item):
        self.stack1.append(item)
        for i in self.stack1[::-1]:
            self.stack2.append(i)

    def remove(self):
        self.stack2.pop(len(self.stack2)-1)

    def size(self):
        return len(self.stack2)


queue = QUEUE_from_stack()

queue.add_que(1)
queue.add_que(2)
queue.add_que(3)
queue.add_que(4)

queue.remove()
queue.remove()
print(queue.low())