
# PROBLEM 1     sum

def sum_to_n(n):

    if n==0:
        return 0

    else:
        return n+sum_to_n(n-1)


# PROBLEM 2     splited sum

def split_sum(num):

    if num%10 == int(str(num)[0]):
        return num

    else:
        return num%10 + split_sum(num//10)


# PROBLEM 3     word match

def word_split(string,list,output=None):

    if output==None:
        output = []

    else:
        for words in list:
            if words in string:

                sl = slice(0, len(words) - 1)

                string = string[sl]

                output.append(words)

                return word_split(string,list,output)

        return output

string = 'themanran'

list = ['the' , 'man' , 'ran']

print(word_split(string,list))