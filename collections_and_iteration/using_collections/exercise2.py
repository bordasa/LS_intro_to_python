my_string = 'Launch School'
first_c = my_string.find('c')

if (first_c + 6) <= (len(my_string) - 1):
    print(my_string[first_c : first_c + 6])
