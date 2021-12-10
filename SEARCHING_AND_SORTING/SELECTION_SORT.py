import random

def Selection_sort_max(list): # maximum tracker
    # iterate list in reverse index like 4,3,2,1,0 index
    for i in range(len(list)-1,-1,-1):
        # set greatest index is 0
        greatest_index = 0
        # iterate through i+1 indexes and cheque for greatest element index
        for j in range(i+1):
            if list[j] > list[greatest_index]:
                greatest_index = j
        # swap greatest index elment with lst element
        list[i] , list[greatest_index] = list[greatest_index] , list[i]
    # return sorted list
    return list


def Selection_sort_min(list): # minimum tracker
    # get index in order from 0 to lenth of list - 1
    for i in range(len(list)):
        # hence after iterations smalest elem are at the less than i th index
        # set minimum index to i
        min_index = i
        for j in range(i,len(list)):
            if list[j] < list[min_index]:
                min_index = j
        # swap minimum index with i which is 0 then 1,2,3 .... lenth of list
        list[i] , list[min_index] = list[min_index] , list[i]
    # return sorted list
    return list



data = []
for _ in range(10000):
    data.append(random.randint(0,10000))

# print(Selection_sort_max(data))
print(Selection_sort_min(data))
