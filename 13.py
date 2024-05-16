def sum_of_whole_list(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum
list = [-1,3,4]
check = sum_of_whole_list(list)
print(check)