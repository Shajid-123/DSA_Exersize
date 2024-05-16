def divisible_by_5_and_11(number):
    if number % 5 == 0 and number % 11 == 0:
        return "divisible"
    else:
        return "not divisible"
    
number = 110
divisible_check = divisible_by_5_and_11(number)
print(divisible_check)