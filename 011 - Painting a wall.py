height = float(input('What is the height of the wall? \n Answer: '))
width = float(input('What is the width of the wall? \n Answer: '))
size = height * width
paint = size/2
print(f'For painting {size}m², you gonna need {paint:.3f}L of paint.')