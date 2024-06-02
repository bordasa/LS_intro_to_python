balance = 1000
interest = .05
years = 5

for i in range(1, (years + 1)):
    balance *= (1 + interest)

print(round(balance, 2))

other_balance = (1000 * 1.05 * 1.05 * 1.05 * 1.05 * 1.05)
print(round(other_balance), 2)