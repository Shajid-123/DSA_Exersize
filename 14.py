def max_and_min(list):
    maximum = max(list)
    minimum = min(list)
    return f'Max = {maximum}, Min = {minimum}'

list = [5,6,7,20,3,100]

check = max_and_min(list)
print(check)
