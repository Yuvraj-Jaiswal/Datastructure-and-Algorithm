
def Insertion_sort(list):

    for k in range(1, len(list)):

        currentvalue = list[k]

        while list[k - 1] > list[k] and k > 0:

            list[k] = list[k - 1]
            k -= 1

        list[k] = currentvalue

    return list

list = [1,2,6,5]
print(Insertion_sort(list))