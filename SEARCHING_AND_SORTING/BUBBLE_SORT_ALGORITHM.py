import random

def Bubble_sort(list):

    for i in range(len(list)):

        for j in range(1, len(list)-i):
            if list[j - 1] > list[j]:

                list[j], list[j - 1] = list[j - 1], list[j]

    return list



def Bubble_sort_2(list):

    for i in range(len(list)-1 , 0 , -1):

        for j in range(i):
            if list[j] > list[j+1]:
                list[j] , list[j+1] = list[j+1] , list[j]

    return list



data = []
for _ in range(10000):
    data.append(random.randint(0,10000))

print(Bubble_sort_2(data))
