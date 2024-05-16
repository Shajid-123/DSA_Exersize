def check_character_type(char):
    if char.isalpha():
        return f"{char} is an alphabet."
    elif char.isdigit():
        return f"{char} is a digit."
    else:
        return f"{char} is a special character."
    
char = input("Enter a Char: ")
check = check_character_type(char)
print(check)


