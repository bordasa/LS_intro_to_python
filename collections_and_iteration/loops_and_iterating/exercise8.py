my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

new_dict = {f'{element}': len(element)
            for element in my_set
            if len(element) % 2 != 0}

print(new_dict)