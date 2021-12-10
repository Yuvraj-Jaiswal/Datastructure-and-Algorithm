
string = '     this    is my   house'
# 'house my is this'


list = []       # best solution
word = ''
for i in range(len(string)):

    if string[i].isalpha():
        word = word+string[i]
        if i == len(string) - 1:
            list.append(word)

    else:
        if word!='':
            list.append(word)

        word = ''

for j in range(len(list)-1 , -1 , -1):
    print(list[j] , end='')
    print(' ' , end='')

#%%
list = []
word = ''
for i in string:
    if i==' ':
        list.append(word)
        word = ''
    else:
        word += i

for j in range(len(list)-1 , 0-1 , -1):
    print(list[j] , end='')
    print(' ' , end='')


#%%

words = string.split(' ')

for i in range(len(string)):
    if string[i]==' ':
        words.pop(0)
    else:
        break

for j in string[::-1]:
    if j==' ':
        words.pop(len(words)-1)
    else:
        break

print(" ".join(words[::-1]))



