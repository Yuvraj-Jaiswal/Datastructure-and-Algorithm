
class node():

    def __init__(self,value):

        self.value = value
        self.nextnode = None


def reverese_list(head):

    current = head
    previous = None
    next = None

    while current:

        next = current.nextnode

        current.nextnode = previous

        previous = current

        current = next

    return previous


a = node(1)
b = node(2)
c = node(3)

a.nextnode = b
b.nextnode = c

reverese_list(a)

print(a.nextnode)
print(b.nextnode.value)
print(c.nextnode.value)
print(c.value)
