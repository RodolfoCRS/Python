estudantes = {}
estudantes['nome'] = str(input('Aluno: '))
estudantes['media'] = float(input(f'Media de {estudantes["nome"]}: '))
if estudantes['media'] >= 7:
    estudantes['Situação'] = 'Aprovado'
elif 5 <= estudantes['media'] < 7:
     estudantes['Situação'] = 'Recuperação'
else:
 estudantes['Situação'] = 'Reprovado'
print("-=" * 30)
for k, v in estudantes.items():
    print(f'{k} é igual a {v}')