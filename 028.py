from random import randint
print('-'*15 + 'GUESS THE NUMBER GAME' + '-'*15)
a = randint(0,5)
print('The computer choose a number between 0 and 5.')
b = int(input('Try to guess the number: '))
if b == a:
    print('Congratulations! \n The computer choose the number: {} \n You choose: {} '.format(a,b))
else:
    print('You lose. \n The computer choose the number: {} \n You choose: {} '.format(a,b))