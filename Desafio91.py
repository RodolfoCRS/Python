from random import randint
from time import sleep
from operator import itemgetter
banco = {'jogador1' : randint(1, 6),
         'jogador2' : randint(1, 6),
         'jogador3' : randint(1, 6),
         'jogador4' : randint(1, 6)}
ranking = ()
print('Valores sorteados:')
for k, v in banco.items():
    print(f'{k} tirou {v}')
ranking = sorted(banco.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking, start = 1):
    print(f'{i}º Lugar: {v[0]} com {v[1]} pontos no dado.')
