my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(my_tuple):
    return [item 
            for item in my_tuple 
            if type(item) is int]

print(find_integers(my_tuple))