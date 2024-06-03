age = input('How old are you? \n')

print(f'You are {age} years old.')

for i in [10, 20, 30, 40]:
    new_age = int(age) + i
    print(f'In {i} years, you will be {new_age} years old.')