dados = dict()
dados['nome'] = str(input("Nome do Jogador: "))
dados['partida'] = int(input(f"Quantas partidas {dados['nome']} jogou? "))
dados['gols'] = list()
partidas = dados['partida']
for i in range(1, partidas+1):
    dados['gols'].append(int(input(f"Quantos gols na partida {i} ? ")))
print(dados) 
dados['total'] = sum(dados['gols'])
print('-=' * 30)
for k,v in dados.items():
    if (k != 'partida'):
        print(f'O campo {k} tem o valor de {v}.')
print('-=' * 30)
print("O jogador " + dados['nome'] + " Jogou" , dados['partida']," Partidas")
for count, x in enumerate(dados['gols']):
    print(f'=> Na partida {count+1}, fez {x} gols')
print(f"Foi um total de {dados['total']} gols")