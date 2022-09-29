a = str(input('Digit your full name: ')).title().strip()
b = a.split()
print('Your first name is: {}'.format(b[0]))
print('Your last name is: {}'.format(b[-1]))
