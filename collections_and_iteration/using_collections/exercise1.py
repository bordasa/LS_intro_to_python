i = 0

for num in range(0, 25, 3):
    i += 1
    if i == 7:
        print(num)

# Suggested Solution

my_range = list(range(0, 25, 3))
print(my_range[6])