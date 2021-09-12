#ex001
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
#ex002
nome = str(input('Qual o seu nome? '))
print(f'Bom Dia {nome}')
if nome == 'Maycon':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal')
#ex003
n1 = float(input('Digite sua primeira nota'))
n2 = float(input('Digite sua segunda nota'))
media = (n1 + n2) / 2
if media >= 6 :
    print('Sua média foi boa')
else:
    print('Estude Mais')
print('parabéns' if media >=6 else 'Estude mais')