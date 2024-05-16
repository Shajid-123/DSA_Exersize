def upper_or_lower(alpha):
    if alpha.isupper():
        return 'Upper'
    elif alpha.islower():
        return 'Lower'
    else:
        return 'Invalid'
    
alpha = 'A'
check = upper_or_lower(alpha)
print(check)