a = int(input('Digit a number between 0 and 9999. \n -> '))
u = a // 1 % 10
t = a // 10 % 10
h = a // 100 % 10
th = a // 1000 % 10
print(f' Unit: {u} \n Tens: {t} \n Hundreds: {h} \n Thousands: {th}')