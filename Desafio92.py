from ast import Delete
from datetime import datetime

dados = {}
dados['nome'] = str(input("Digite seu nome: "))
ano = int(input("Ano de nascimento: "))
dados['idade'] = (datetime.today().year) - ano
dados['carteira'] = int(input("CTPS (0 não tem): "))
if dados['carteira'] != 0:
    dados['contratação'] = int(input("Ano de contratação: "))
    dados['salario'] = float(input("Salário R$: "))
    dados['aposentadoria'] = dados ['idade'] + ((dados['contratação'] + 35) - datetime.today().year)
else:
    del dados['carteira']
print('=-=' * 30) 
for k, v in dados.items():
    print(f'{k} tem o valor de {v}')