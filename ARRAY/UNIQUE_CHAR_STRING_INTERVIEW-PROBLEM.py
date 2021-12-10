
string = 'abcde'
x = 1

for i in range(len(string)):        # bruteforce solution
    for j in range(len(string)):
        if i!=j:
            if string[i]==string[j]:
                x = 0
                break
            else:
                x = 1

if x==1:
    print('TRUE')
else:
    print('FALSE')


#%%

dict = {}       # hash map , dictionary solution
x = 1

for i in string:

    if i in dict:
        dict[i] += 1

    else:
        dict[i] = 1

for k in dict.values():
    if k > 1:
        x = 0
        break

    else:
        x = 1

if x==1:
    print('TRUE')
else:
    print('FALSE')

