print('-=' * 20)
print(' ' * 6 + 'Sum odd multiples of three')
print('-=' * 20)
s = 0
for i in range(1,500):
    if i%2 != 0:
        if i%3 == 0:
            s += i
print(s)