a = int(input('Enter with the first value: '))
b = int(input('Enter with the second value: '))
c = int(input('Enter with the third value: '))
lista = [a,b,c]
list.sort(lista)
print('The lower value is: {}'.format(lista[0]))
print('The higher value is: {}'.format(lista[2]))