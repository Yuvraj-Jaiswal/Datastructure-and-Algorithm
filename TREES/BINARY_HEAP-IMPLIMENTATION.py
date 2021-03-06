
class Binary_Heap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def swap_parent(self,i):
        while i*2 <= self.current_size:
            min_child = self.min_child(i)
            # i mean parent and i//2 mean child     i is index
            if self.heap_list[i] > self.heap_list[min_child]:
                self.heap_list[i] , self.heap_list[min_child] = self.heap_list[min_child] , self.heap_list[i]
            i = min_child

    def min_child(self,i):
        if i*2 + 1 > self.current_size:
            return i*2
        else:
            if self.heap_list[i*2] >self.heap_list[i*2+1]:
                return i*2
            else:
                return i*2+1

    def insert(self,k):
        self.heap_list.append(k)
        self.current_size += 1
        self.swap_parent(self.current_size)

    def del_min(self):
        min = self.heap_list[1]
        self.heap_list.pop()
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.swap_parent(1)
        return min

    def build_heap_list(self,list):
        i = len(list)//2
        self.current_size = len(list)
        self.heap_list = [0] + list[:]
        while (i>0):
            self.swap_parent(i)
            i -= 1

