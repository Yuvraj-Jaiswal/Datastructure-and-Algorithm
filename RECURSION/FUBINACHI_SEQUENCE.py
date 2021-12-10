
def fubinachi(n):

    if n > 2:
        return fubinachi(n-1) + fubinachi(n-2)

    elif 0 < n <= 2:
        return 1

def fub2(n):
    fub = [1,1]

    for i in range(2,n):
        num = fub[i-1] + fub[i-2]
        fub.append(num)

    return fub[-1]

def fub_iteraive(n):

    x = 1
    y = 1

    for i in range(2,n):
        x , y = y , x+y

    return y

casch = [None] * (10+1)

def fub_dy_rec(n):

    if n==1 or n==2:
        return 1

    if casch[n] != None:
        return casch[n]

    else:
        casch[n] = fub_dy_rec(n-1) + fub_dy_rec(n-2)
        
    return casch[n]


print(fub_dy_rec(10))