def check_vowel_consonant(char):
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    if char.lower() in vowels:
        return f"{char} is a vowel."
    elif char.isalpha():
        return f"{char} is a consonant."
    else:
        return f"{char} is not a valid alphabet."
    
char = input("Enter an alphabet: ")
check = check_vowel_consonant(char)
print(check)




