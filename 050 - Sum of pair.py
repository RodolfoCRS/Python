print('-=' * 22)
print('Sum of pair')
print('-=' * 22)
sum = 0
for i in range(1,7):
    number = int(input('Enter with a number: '))
    if number %2 == 0:
        sum += number
print('The sum of the pairs is: {}'.format(sum))