from datetime import date
print('-=-'*20)
print(' '*20 + 'Military enlistment')
print('-=-'*20)

yob = int(input('Enter with your year of birth: '))
yn = date.today().year - yob
if yn < 18:
    print('You will have to enlist in {} years'.format(18-yn))
elif yn == 18:
    print('Its time to you enlist.')
else:
    print('You should have enlisted {} years ago'.format(yn-18))