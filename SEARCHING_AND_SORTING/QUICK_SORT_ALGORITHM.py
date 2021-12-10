import random
from time import  time
def Quick_sort(list):

    if len(list) <= 1:
        return list

    left = []
    right = []
    piv_list = []
    pivit_point = list[random.randint(0,len(list)-1)]

    for i in list:
        if i<pivit_point:
            left.append(i)
        elif i>pivit_point:
            right.append(i)
        else:
            piv_list.append(i)

    return Quick_sort(left) + piv_list + Quick_sort(right)

data = []
for _ in range(1000000):
    data.append(random.randint(0,2))

t0 = time()
print(Quick_sort(data))
t1 = time()
print('time taken is : ' , t1-t0)