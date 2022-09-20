a = float(input('Digit a value in meters to convert: '))
print('The value is: {:.0f} millimeters'.format(a*1000))
print('The value is: {:.0f} centimeters'.format(a*100))
print('The value is: {:.0f} decimeter'.format(a*10))
print('The value is: {:.3f} dekameter'.format(a/10))
print('The value is: {:.3f} hectometer'.format(a/100))
print('The value is: {:.3f} kilometer'.format(a/1000))

