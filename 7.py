def is_alphabet(char):
    if char.isalpha():
        return 'Alphabet'
    else:
        return 'not Alphabet'


char = '@'
check = is_alphabet(char)
print(check)