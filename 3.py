def negetive_positive_zero(number):
    if number < 0:
        return 'negetive'
    elif number == 0:
        return 'zero'
    else:
        return 'positive'
    
number = 0 
catagory = negetive_positive_zero(number)
print(catagory)