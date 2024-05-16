def count_neg(list):
    count = 0
    for i in list:
        if i < 0:
            count = count+1
    return f'Num of negetive numbers: {count}'

list = [-1,-2,-3,-4,4,5,6,7]

check = count_neg(list)
print(check)