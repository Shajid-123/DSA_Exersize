def read_list():
    n = int(input("Enter the number of elements: "))
    list = []
    for i in range(n):
        element = input(f"Enter element {i+1}: ")
        list.append(element)
    return list

def print_list(list):
    print("Elements of the list:")
    for element in list:
        print(element)
list = read_list()
check = print_list(list)


