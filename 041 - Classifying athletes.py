print('-=-'*20)
print(' '*20 + 'Classifying athletes')
print('-=-'*20)

age = int(input('Enter with the age of the athlete: '))
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