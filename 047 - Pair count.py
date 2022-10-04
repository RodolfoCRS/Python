print('-=' * 20)
print(' ' * 14 + 'Pair count')
print('-=' * 20)

number = int(input('Enter with the number and the program will show only the pair numbers between 0 and your '
                   'number.\n --> '))
for i in range(0, number+2, 2):
    print(i)