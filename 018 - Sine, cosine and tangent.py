import math
a = int(input('Digit the angle: '))
a = math.radians(a)
print('The sine: {:.2f} \nThe cosine: {:.2f} \nThe tangent: {:.2f}'.format(math.sin(a), math.cos(a), math.tan(a)))