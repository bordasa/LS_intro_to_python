first_num = input('Enter the first number: ')
second_num = input('Enter the second number: ')

def multiply(num1, num2):
    num1 = float(num1)
    num2 = float(num2)

    print(f'{num1} * {num2} = {num1 * num2}')

multiply(first_num, second_num)