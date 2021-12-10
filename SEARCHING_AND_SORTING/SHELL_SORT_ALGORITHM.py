
def Insertion_sort(list,start,gap):

    for k in range(start+gap, len(list) , gap):

        currentvalue = list[k]

        while list[k - gap] > list[k] and k > 0:

            list[k] = list[k - gap]
            k -= gap

        list[k] = currentvalue

    return list


def Insertion_sort_gap_maker(list):

    sublist = len(list)//2

    while sublist > 0:

        for start in range(sublist):

            Insertion_sort(list,start,sublist)

        sublist = sublist//2