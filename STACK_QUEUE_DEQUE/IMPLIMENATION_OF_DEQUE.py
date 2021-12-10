
class DEQUE():

    def __init__(self):
        self.deque = []

    def add_front(self,item):
        self.deque.insert(0,item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        self.deque.pop(0)

    def remove_rear(self):
        self.deque.pop(len(self.deque)-1)

    def size(self):
        return len(self.deque)

    def peak(self):
        return self.deque[len(self.deque)-1]

    def low(self):
        return self.deque[0]

    def isempty(self):
        return self.deque == []

deque = DEQUE()

