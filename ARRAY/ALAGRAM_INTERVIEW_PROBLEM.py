str1 = 'god'
str2 = 'd g o'

for i in str1:
    if i==' ':
        str1 = str1.replace(i,'').lower()

for j in str2:
    if j==' ':
        str2 = str2.replace(j,'').lower()

#%%

for i in str1:      # bruteforse solution
    x = 0
    for j in str2:
        if i==j:
            x = 1

    if x == 1:
        pass
    else:
        break

if x==1:
    print('true')
else:
    print('false')


#%%

dict = {}   # solution 1 dictionary
x = 1

for i in str1:
    if i in dict:
        dict[i] = dict[i] + 1
    else:
        dict[i] = 1

for j in str2:
    if j in dict:
        dict[j] = dict[j] - 1
    else:
        dict[j] = 1

for k in dict:
    if dict[k] != 0:
        x = 0
        break

if x == 0:
    print('FALSE')
else:
    print('TRUE')

#%%


x = 1
if len(str1)!=len(str2): # solution 2
    print('FALSE')
else:
    for i in str1:
        if i in str2:
            x = 1
        else:
            x = 0
            break
    if x == 0:
        print('FALSE')
    if x == 1:
        print('TRUE')







