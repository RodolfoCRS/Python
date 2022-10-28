print('-=' * 22)
print(' ' * 14 + 'Prime number')
print('-=' * 22)

number = int(input("Digit the number: "))
cont = 0
for i in range(1, number+1):
    if number%i == 0:
        print("\033[32m{}\033[m".format(i), end=' ')
        cont += 1
    else:
        print("\033[31m{}\033[m".format(i), end=' ')
if cont == 2:
    print("\nThe number is prime")
else:
    print("\nThe number is not prime")