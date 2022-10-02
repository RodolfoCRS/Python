print('-=-'*20)
print(' '*20 + 'That average classic')
print('-=-'*20)

firstresult = float(input('Enter with the student first test result: '))
secondresult = float(input('Enter with the student second result: '))
avarage = (firstresult + secondresult)/2
print('The average is: {}'.format(avarage))
if avarage < 5:
    print('The student did not reach the average')
elif 5 <= avarage <= 6.9:
    print('The student is in recovery')
else:
    print('The student is approved.')