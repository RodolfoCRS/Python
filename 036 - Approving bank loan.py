print('-=-'*20)
print(' '*20 + 'Approving bank loan')
print('-=-'*20)

housevalue = float(input('What is the value of the house? \n $: '))
salary = float(input('What is the value of your salary? \n $: '))
timetopay = int(input('How many years would you like to pay? \n Years: '))

mpay = housevalue / (timetopay*12)
if mpay >= (salary*0.3):
    print('Unfortunately your loan was \033[0;31m DENIED \033[m\nInstallment value: ${:.2f}'.format(mpay))
    print('Your salary must be {:.2f} to be \033[0;32m APPROVED \033[m'.format(mpay/0.3))
else:
    print('Congratulations, your loan was been \033[0;32m APPROVED \033[m\nInstallment value: ${:.2f}'.format(mpay))
