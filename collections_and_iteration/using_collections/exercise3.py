tup1 = (1, 2, 3, 4, 5)

new_tup = tup1[-2 : 0 : -1]

print(new_tup)

# different solution

reversed_tup = tuple(reversed(tup1))
result = reversed_tup[1:len(reversed_tup) - 1]
print(result)