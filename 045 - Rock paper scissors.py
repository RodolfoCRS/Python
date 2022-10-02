from random import randint
from time import sleep

print('-='*20)
print(' '*10 + 'Rock paper scissors')
print('-='*20)

computerchoice = randint(1,3)

humanchoice = int(input('Choose an option:\n 1 --> Rock\n 2 --> Paper\n 3 --> Scissors\n Choice: '))
print('Rock! Paper! Scissors!')
sleep(1)
print('1!')
sleep(1)
print('2!')
sleep(1)
print('3!\n')
sleep(2)
if computerchoice == 1 and humanchoice == 2:
    print('The computer choose: ROCK\n'
          'You choose: PAPER \n\033[32;40mYOU WIN!!!\033[m')
elif computerchoice == 1 and humanchoice == 3:
    print('The computer choose: ROCK\n'
          'You choose: SCISSORS \n\033[31;40mYOU LOSE!!!\033[m')
elif computerchoice == 2 and humanchoice == 1:
    print('The computer choose: PAPER\n'
          'You choose: ROCK \n\033[31;40mYOU LOSE!!!\033[m')
elif computerchoice == 2 and humanchoice == 3:
    print('The computer choose: PAPER\n'
          'You choose: SCISSORS \n\033[32;40mYOU WIN!!!\033[m')
elif computerchoice == 3 and humanchoice == 1:
    print('The computer choose: SCISSORS\n'
          'You choose: ROCK \n\033[32;40mYOU WIN!!!\033[m')
elif computerchoice == 3 and humanchoice == 2:
    print('The computer choose: SCISSORS\n'
          'You choose: PAPER\n\033[31;40mYOU LOSE!!!\033[m')
else:
    print('Its a DRAW!')