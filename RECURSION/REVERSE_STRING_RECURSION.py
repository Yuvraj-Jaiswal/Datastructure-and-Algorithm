

def reverse_string(str):    # using slice

    if len(str) <= 1:
        return str

    else:
        sl = slice(0,len(str)-1)
        return str[len(str)-1] + reverse_string(str[sl])


def reverse_string_sol_2(str):    # using itteraator

    if len(str) <= 1:
        return str

    else:
        sl = ''
        for i in range(len(str)-1):
            sl = sl + str[i]

        return str[len(str) - 1] + reverse_string(sl)

str = 'hellow'      #wolleh

print(reverse_string_sol_2(str))