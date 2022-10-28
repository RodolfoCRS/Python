print('-=' * 22)
print('Sum odd multiples of three between 1 and 500')
print('-=' * 22)
s = 0
for i in range(1,500):
    if i%2 != 0:
        if i%3 == 0:
            s += i
print('The sum odd multiples of three between 1 and 500 is: {}'.format(s))