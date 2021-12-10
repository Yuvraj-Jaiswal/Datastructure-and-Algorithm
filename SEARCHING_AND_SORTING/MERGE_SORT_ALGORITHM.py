import random

def Merge(left,right):
    list = []   # set an empty list which merge two array in sortd manner
    i,j = 0 ,0    # set index for left and right
    # appent smalest element until indexes is less than lenth of left and right
    while i < len(left) and j < len(right):
        # cheque which elem is smalest and append to list and then increase index
        # by 1
        if left[i] < right[j]:
            list.append(left[i])
            i += 1
        else:
            list.append(right[j])
            j += 1
    # if any of the left or right is fully used then append
    #  remaining elemnt of other in list
    list += left[i:]
    list += right[j:]
    #  return merged list
    return list

def Merge_sort(list):
    # if length of list is 1 return list
    if len(list) <= 1:
        return list
    # set mid index
    mid = len(list)//2
    left = Merge_sort(list[:mid])   # recursively use merge sort until lenth
    # of elemnts are 1
    right = Merge_sort(list[mid:])  # recursively use merge sort until lenth
    # of elemnts are 1

    # when all elements are of lenth 1 then merge every right left pair in order
    # return sorted list
    return Merge(left,right)



print(pow(2,30))
