print('-=-'*20)
print(' '*20 + 'Payment manager')
print('-=-'*20)

price = float(input('Enter with the product price: $'))
method = int(input('\n1 - Spot price with MONEY (Discount: -10%)\n'
                   '2 - Spot price with CARD (Discount: -5%)\n'
                   '3 - 2x with CARD (Discount: 0%)\n'
                   '4 - 3x or more with CARD (Rise: 20%)\n'
                   'Choose your payment method: '))
if method == 1:
    price = price-(price*0.1)
    print('\n The final price of the product is: ${:.2f}'.format(price))
elif method == 2:
    price = price-(price*0.05)
    print('\n The final price of the product is: ${:.2f}'.format(price))
elif method == 3:
    print('\n The final price of the product is: ${:.2f}'.format(price))
elif method == 4:
    price = price+(price*0.20)
    print('\n The final price of the product is: ${:.2f}'.format(price))
else:
    print('\n Choose a valid option.')



