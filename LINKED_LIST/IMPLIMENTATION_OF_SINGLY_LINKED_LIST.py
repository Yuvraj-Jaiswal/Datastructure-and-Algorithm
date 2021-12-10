
class Linklist_singly():

    def __init__(self,value):

        self.value = value
        self.nextnode = None


a = Linklist_singly(1)
b = Linklist_singly(2)
c = Linklist_singly(3)

a.nextnode = b
b.nextnode = c


print(a.nextnode.value)