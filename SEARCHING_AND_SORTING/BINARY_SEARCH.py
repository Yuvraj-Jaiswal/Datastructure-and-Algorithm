
def Binary_search(elem,list_O):

    low = 0
    high = len(list_O)-1

    found = False

    while high >= low and found==False:
        mid_index = (high+low)//2

        if list_O[mid_index] == elem:
            found = True

        elif elem < list_O[mid_index]:
            high = mid_index - 1

        else:
            low = mid_index + 1

    return found


def Binary_search_recursion(elem,list):

   mid_index = len(list)//2

   if len(list)==1 and list[mid_index]!=elem:
       return False

   if list[mid_index] == elem:
       return True

   else:
        if elem < list[mid_index]:
            list = list[:mid_index]
            Binary_search_recursion(elem,list)

        else:
            list = list[mid_index:]
            Binary_search_recursion(elem,list)


print(Binary_search(5,[1,2,3,4,6,8,9]))