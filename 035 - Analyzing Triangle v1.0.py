a = float(input('Enter with the first side: '))
b = float(input('Enter with the second side: '))
c = float(input('Enter with the third side: '))

if a < b+c and b < a+c and c < b+a:
    print('You\033[1;32;40m can \033[mform a triangle with this sizes of side.')
else:
    print('You\033[1;31;40m cant \033[mform a triangle with this sizes of side.')

