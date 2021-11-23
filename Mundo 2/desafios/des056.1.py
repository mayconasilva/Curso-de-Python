somaidade = 0
maioridadehomem = 0
mediaidade = 0
nomevelho = 0
totmulher20 = 0
for c in range(1, 5):
    name = str(input(f'Por favor, digite o nome da {c}ª pessoa: '))
    idade = int(input(f'Por favor, digite a idade da {c}ª pessoa: '))
    sexo = str(input(f'Por favor, digite o sexo da {c}ª pessoa: (masculino ou feminino)'))

    somaidade += idade

    if c == 1 and sexo in"Mm":
            maioridadehomem = idade
            nomevelho = name
    if sexo in "Mm" and idade > maioridadehomem:
            maioridadehomem = idade
            nomevelho = name
    if sexo in "Ff" and idade < 20:
            totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média do idade do grupo é de {mediaidade} anos')
print(f'O homem mais velho se chama {nomevelho} e possui {maioridadehomem}')
print(f'Ao todo {totmulher20} possui menos de 20 anos')

