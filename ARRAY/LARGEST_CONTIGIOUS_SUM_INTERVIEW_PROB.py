
array = [1,80,-3,4,5,13,-40]

max_sum = current_sum = array[0]

for num in array[1:]:

    if current_sum + num > num:
        current_sum = current_sum + num

    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)


#%%

max_ending_here = 0
max_soo_far = array[0]
start = 0
end = 0
s = 0

for i in range(len(array)):
    max_ending_here = max_ending_here + array[i]

    if max_soo_far < max_ending_here:
        max_soo_far = max_ending_here
        start = s
        end = i

    if max_ending_here < 0:
        max_ending_here = 0
        s = i+1

print(max_soo_far)

#%%









