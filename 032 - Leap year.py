from datetime import date
a = int(input('Enter with the year you want to analyze. "Enter with 0 if you wanna know about the current year": '))
if a == 0:
    a = date.today().year
if a%4 == 0 and a%100 != 0 or a%400 == 0:
    print('The year of {} is a leap year.'.format(a))
else:
    print('The year of {} is not a leap year.'.format(a))