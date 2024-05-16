def second_largest(list):
    maximum = max(list)
    list.remove(maximum)
    second_max = max(list)
    return second_max

list = [3,4,5,1,10,20,50]

check = second_largest(list)

print(check)