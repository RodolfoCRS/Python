from datetime import date
print('-=-'*20)
print(' '*20 + 'Classifying athletes')
print('-=-'*20)

yb = int(input('Enter with the year of birth of the athlete: '))
age = date.today().year - yb
print('The athlete is {} years old.'.format(age))
if age <= 9:
    print('This athlete is classified as a child.')
elif 9 < age <= 14:
    print('This athlete is classified as juvenile.')
elif 14 < age <= 19:
    print('This athlete is classified as junior.')
elif 19 < age <= 20:
    print('This athlete is classified as senior.')
else:
    print('This athlete is classified as master.')