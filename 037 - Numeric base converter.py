print('-=-'*20)
print(' '*20 + 'Numeric base converter')
print('-=-'*20)

number = int(input('Enter with a number: '))
choice = int(input('Choose your base converter: \n 1 - \033[1;30;42mBinary\033[0m \n 2 - \033[1;30;42mOctal\033[0m \n 3 - \033[1;30;42mHexadecimal\033[0m \n --> '))
if choice == 1:
    numberbin = bin(number)
    print('The number {} in binary is: {}'.format(number, numberbin))
elif choice == 2:
    numberoct = oct(number)
    print('The number {} in octal is: {}'.format(number, numberoct))
elif choice == 3:
    numberhex = hex(number)
    print('The number {} in hexadecimal is: {}'.format(number, numberhex))
else:
    print('Choose a valid option.')
