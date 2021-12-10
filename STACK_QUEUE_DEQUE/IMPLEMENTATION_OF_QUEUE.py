
class QUEUE():

    def __init__(self):
        self.queue = []

    def add(self,item):
        self.queue.append(item)

    def remove(self):
        self.queue.pop(0)

    def isempty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)

    def low(self):
        return self.queue[0]

queue = QUEUE()


