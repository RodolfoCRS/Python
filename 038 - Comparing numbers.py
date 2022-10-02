print('-=-'*20)
print(' '*20 + 'Comparing numbers')
print('-=-'*20)

firstvalue = int(input('Enter with the first value to be compare: '))
secondvalue = int(input('Enter with the second value to be compare: '))
if firstvalue > secondvalue:
    print('The first value is greater than the second value {}'.format(firstvalue, secondvalue))
elif firstvalue < secondvalue:
    print('The second value is greater than the first value {}'.format(secondvalue, firstvalue))
else:
    print('The first value is equal to the second value'.format(firstvalue, secondvalue))
