print('-=-'*20)
print(' '*20 + 'Comparing numbers')
print('-=-'*20)

firstvalue = int(input('Enter with the first value to be compare: '))
secondvalue = int(input('Enter with the second value to be compare: '))
if firstvalue > secondvalue:
    print('The value {} is greater than the value {}'.format(firstvalue, secondvalue))
elif firstvalue < secondvalue:
    print('The value {} is greater than the value {}'.format(secondvalue, firstvalue))
else:
    print('The value {} is equal to the value {}'.format(firstvalue, secondvalue))
