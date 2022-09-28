from random import shuffle
thelist = []
for i in range(4):
    a = str(input('Digit something to be randomly sorted: '))
    thelist.append(a)
shuffle(thelist)
print('The randomly sorted items are: {}'.format(thelist))