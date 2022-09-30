a = int(input('Enter the distance of the trip in Km: '))
if a < 200:
    print('The price of the passage is: {}$'.format(a*0.5))
else:
    print('The price of the passage is: {}$'.format(a*0.45))
