balance = 1000
interest = .05
years = 5

for i in range(1, (years + 1)):
    balance *= (1 + interest)
    print(f'Current Balance in year: {i}')
    print(round(balance, 2))
