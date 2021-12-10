
list = [1,2,3,4,5,6,89]
sum = 5


seen = set()       # best solution set data_structure
count = 0
for elem in list:
    req = sum - elem
    if req in seen:
        print([elem,req])
        count += 1
    else:
        seen.add(elem)

print(count)
#%%

dict = {}   # bruteforce solution
for i in list:
    for j in list:
        if i!=j:
            if i+j==sum:
                if i and j not in dict:
                    dict[i] = j

print(dict)

#%%

j = len(list) - 1       # soution 1 if array is sorted
i = 0
for _ in range(len(list)):

    if i < j:
        if list[i]+list[j] == sum:
            print([i,j])
            i = i + 1

        elif list[i] + list[j] > sum:
            j = j - 1

        else:
            i = i + 1

    else:
        break


#%%

dict = {}       # hash-map , dictionary solution

for i in list:
    if i in dict:
        print([i,dict[i]])
    else:
        req = sum - i
        dict[req] = i







