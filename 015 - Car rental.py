days = int(input('For how many days was the car rented? \n Answer: '))
km = float(input('How many kilometers were driven? \n Answer: '))
days = days * 60
km = km * 0.15
total = days + km
print('You must pay ${:.2f}'.format(total))

