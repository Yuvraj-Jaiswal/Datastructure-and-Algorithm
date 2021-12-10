
dict = {'paisa' : 0 , 'raju' : -1000 , 'shayam' : 1000 , 'babu_bhiya' : 10}

dict.copy()     # return copy of currnet dictionary

dict.pop('paisa')    # delete element with given key

key = dict.keys()   # return all keys of dictionary

value = dict.values()   # return vaues in dictionary

dict.get('raju')    # return value by giving key

dict['laptop'] = 'nahi he' # append by giving value and key

dict.update({'paisa' : 0 })  # update dict by giving in dictionary

del dict['paisa']   # delete value and key pair by giving key

len(dict)   # return number of key value pair present in dictionary

dict.items()  # return list of key value pair

for key,value in dict.items():      # loop key value in dictionary
    print(key,value)

print(dict)


