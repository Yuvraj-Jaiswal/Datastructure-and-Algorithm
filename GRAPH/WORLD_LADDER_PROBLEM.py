from GRAPH.GRAPH_ADJECENT_LIST_IMPLIMENTATION import Graph

line = ['this', 'computer' , 'has', '4 gb' ,'ram']
dict = {}
graph = Graph()

for word in line:
    rem_word = word[:-1]
    print(rem_word)
    for i in range(len(word)):
        dashed_word = word[:i] + "_" + word[i + 1:]

        if dashed_word in dict:
            dict[dashed_word].append(rem_word)
        else:
            dict[dashed_word] = [rem_word]

print(dict)