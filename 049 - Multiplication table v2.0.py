print('-=' * 20)
print(' ' * 5 + 'Multiplication Table v2.0')
print('-=' * 20)

number = int(input('Enter with the number to see the Multiplication table: '))
for i in range(1,11):
    result = i*number
    print('{} x {} = {}'.format(number, i , result))