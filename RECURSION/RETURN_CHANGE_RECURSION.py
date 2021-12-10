
coin_list = [1,5,10]
return_amount = 10

output = []

def change(return_amount,coin_list):

    if return_amount<0:
        return None

    else:
        for i in reversed(coin_list):
            if return_amount%i==0 and return_amount-i>=0:
                return_amount -= i
                output.append(return_amount)
                return change(return_amount,coin_list)

change(509,[1,2,10])

print(output)

