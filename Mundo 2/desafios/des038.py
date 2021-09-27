num = int(input("Digite um número inteiro"))
nom = int(input("Digite outro número inteiro"))
if (num > nom):
    print(f'{num} é maion que {nom}')
elif (nom > num):
    print(f'{nom} é maior que {num}')
else:
    print(f'Não existe valor maior, {num} e {nom} são iguais')