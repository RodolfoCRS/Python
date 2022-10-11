estudantes = {}
dados = ()

estudantes['nome'] = str(input('Nome: '))
estudantes['media'] = int(input('Idade: '))
if estudantes['media'] >= 7:
    estudantes['Situação'] = 'Aprovado'
else:
     estudantes['Situação'] = 'Reprovado'

print(f"O aluno {estudantes['nome']} esta {estudantes['Situaçã']}")   
