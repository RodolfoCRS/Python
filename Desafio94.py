pessoa = dict()
galera = list()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input("Digite o nome:"))
    while True:
        pessoa['sexo'] = str(input("Digite o sexo: ")).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print("Erro! digire M ou F.")  
    pessoa['idade'] = int(input("Digite sua idade: "))
    galera.append(pessoa.copy())
    while True:
        resp = str(input("Quer continuar S/N: ")).upper()[0]
        if resp in 'SN':
            break
        print("Escreva S ou N")
    if resp == 'N':
        break
print(galera)
