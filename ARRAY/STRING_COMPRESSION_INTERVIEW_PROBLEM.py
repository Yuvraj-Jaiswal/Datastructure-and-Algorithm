
string = 'AAAAaaaaBBBBCCCCCDDEEEE'
comp_str = ''

dict = {}

for i in string:
    if i in dict:
        dict[i] += 1

    else:
        dict[i] = 1

for key,value in dict.items():
    comp_str += key
    comp_str += str(value)

print(comp_str)

#%%

comp_str = ''
count = 1
current_char = ''

for i in range(1,len(string)):

    if string[i] == string[i-1]:
        count += 1
        if i == len(string) - 1:
            comp_str = comp_str + string[i - 1] + str(count)

    else:
        comp_str = comp_str+string[i-1]+str(count)
        count = 1

print(comp_str)
