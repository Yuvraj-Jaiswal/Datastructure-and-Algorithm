
class STACK():

    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def add(self,item):
        self.stack.append(item)

    def remove_elem(self):
        self.stack.pop(len(self.stack) - 1)

    def size(self):
        return len(self.stack)

    def peak(self):
        return self.stack[len(self.stack)-1]


stack = STACK()

