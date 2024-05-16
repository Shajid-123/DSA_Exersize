def odd_or_even(number):
    if number % 2 == 0:
        return 'even'
    else:
        return 'odd'


number = 19
check = odd_or_even(number)
print(check)