
def ordered_seq_search(elem,list_S):
    pos = 0
    found = False
    greater = False
    while pos < len(list_S) and found != True and greater!=True:

        if list_S[pos]==elem:
            found = True
        elif list_S[pos] > elem:
            found = False
            greater = True

        pos += 1

    return found

def unordered_seq_search(elem,list_US):
    pos = 0
    found = False
    while pos < len(list_US) and found != True:

        if list_US[pos] == elem:
            found = True

        pos += 1

    return found

