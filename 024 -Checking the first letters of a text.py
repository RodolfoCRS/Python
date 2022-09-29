a = str(input('Digit a city name: ')).upper().strip()
b = a.split()
if b[0] == 'SANTO':
    print("The city's name start with SANTO.")
else:
    print("The city's name don't start with SANTO")