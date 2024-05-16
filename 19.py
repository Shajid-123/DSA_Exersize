def fecuency(list):
    print("Frequency of each element:")
    for i in list:
        frequency = len(str(i))
        print(f'{i}: {frequency}')

list = [1,2,3,4,15,56,89]
fecuency(list)