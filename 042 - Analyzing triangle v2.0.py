print('-=-'*20)
print(' '*20 + 'Analyzing triangle v2.0')
print('-=-'*20)

a = float(input('Enter with the first side: '))
b = float(input('Enter with the second side: '))
c = float(input('Enter with the third side: '))
d = 0

if a < b+c and b < a+c and c < b+a:
    print('You\033[1;32;40m can \033[mform a triangle with this sizes of side.')
    if a == b == c:
        print('This triangle is:\033[1;33;40m equilateral \033[m')
    elif a == b and a != c:
        print('This triangle is:\033[1;33;40m isosceles \033[m')
    elif a == c and a != b:
        print('This triangle is:\033[1;33;40m isosceles \033[m')
    elif b == c and b != a:
        print('This triangle is:\033[1;33;40m isosceles \033[m')
    elif a != b != c:
        print('This triangle is:\033[1;33;40m scalene \033[m')
else:
    print('You\033[1;31;40m cant \033[mform a triangle with this sizes of side.')

