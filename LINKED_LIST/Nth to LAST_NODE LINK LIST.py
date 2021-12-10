class node():

    def __init__(self,value):

        self.value = value
        self.nextnode = None


def nth_last(head,index):

    values = []

    while head:

        values.append(head.value)
        head = head.nextnode

    return values[-index]


def solution2(head,index):

    pointer1 = head
    pointer2 = head

    for i in range(index-1):

        pointer1 = pointer1.nextnode

    while pointer1.nextnode:

        pointer1 = pointer1.nextnode
        pointer2 = pointer2.nextnode

    return pointer2.value


a = node(1)
b = node(2)
c = node(3)
d = node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d

print(solution2(a,4))