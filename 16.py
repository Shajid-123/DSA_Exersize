def count_odd_even(list):
    odd = 0
    even = 0
    for i in list:
        if i % 2 == 0:
            even = even+1
        else:
            odd = odd+1
    return f'Number of odd number: {odd}, Number of even number: {even}'

list = [3,5,6,7,8,10,12]

check = count_odd_even(list)
print(check)