a = float(input('Enter the salary to be analyzed: $'))
if a>= 1250:
    a = a + (a*0.1)
else:
    a = a + (a*0.15)
print('The rise of the salary is: ${:.2f}'.format(a))
