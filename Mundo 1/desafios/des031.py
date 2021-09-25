distância = float(input('Qual a distância da viagem? (em km)'))
if distância <= 200:
    print(f'O preço da viagem será de R${distância * 0.5:.2f}')
else:
    print(f'O preço da viagem será de R${distância * 0.45:.2f}')
print('Lembrando que a nossa tabela de preços é: \n Para até 200 km, R$0,45 por km rodado \n Para acima de 200 km, R$0,50 por km rodados')