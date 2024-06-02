def greeter(name, repeat):
    time_of_day = ['Morning', 'Afternoon', 'Evening']

    for i in range(repeat):
        if i < len(time_of_day):
            print(f'Good {time_of_day[i]}, {name}.')
        else:
            print(f'Good Day, {name}.')
 
greeter('Victor', 3)