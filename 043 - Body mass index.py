print('-=-'*20)
print(' '*20 + 'Body mass index')
print('-=-'*20)

height = float(input('Enter with the height: '))
weight = float(input('Enter with the weight: '))
bmi = weight/pow(height,2)
print('You BMI is: {:.0f}'.format(bmi))
if bmi <= 18.5:
    print('BMI indicates: \033[31;40munder weight\033[m')
elif 18.5 < bmi <= 25:
    print('BMI indicates: \033[32;40mideal weight\033[m')
elif 25 < bmi <= 30:
    print('BMI indicates: \033[33;40moverweight\033[m')
elif 30 < bmi <= 40:
    print('BMI indicates: \033[33;40mobesity\033[m')
else:
    print('BMI indicates: \033[31;40mmorbid obesity\033[m')



