velocidade = float(input('Qual a velocidade do carro? (em Km/h) '))
if velocidade > 80:
    print(f'O senhor foi multado por velocidade superior a 80 Km/h. \n O valor dela será deR${(velocidade - 80) * 7:.2f}')
else:
    print('Muito bem!')
print('Tenha um Bom Dia com segurança')