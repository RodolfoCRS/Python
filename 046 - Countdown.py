print('-=' * 20)
print(' ' * 14 + 'Countdown')
print('-=' * 20)

from time import sleep

print('Your computer will burn in.....')
sleep(1)
for i in range(10, 0, -1):
    print(i)
    sleep(1)
print('Just kidding, i dont have this kind of power.......',end='')
sleep(3)
print('\033[0;31;40m YET! \033[0m')
