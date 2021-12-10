list = [1,2,3,4,5,8]
shuffled = [3,1,4,2]

result = 0
for elem in list+shuffled:
    result^=elem
print(result)

#%%

dict = {}       # dictionary soltion 1
for i in shuffled:
    dict[i] = i

for i in list:
    if i not in dict:
        print(i)

#%%
import collections

dict = collections.defaultdict(int)

for i in shuffled:
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

for j in list:
    if dict[j]==0:
        print(j)
    else:
        dict[j] -= 1

#%%

seen = set()    # set solution

for elem in list:
    seen.add(elem)

for i in list:
    if i not in shuffled:
        print(i)

#%%

for elem in list:   # brute_force soution
    x = 0
    for j in shuffled:
        if elem==j:
            x = 1

    if x == 0:
        print(elem)


