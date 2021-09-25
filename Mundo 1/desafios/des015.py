dias = float(input('Quantos dias ficou com o carro?'))
distância = float(input('Rodou o carro em quantos quilometros'))
preçopordia = dias *60
preçoporkm = distância * 0.15
preçofinal = preçopordia + preçoporkm
print(f'O valor por dia será de R${preçopordia} e o por distância será de R${preçoporkm} sendo o preço final de R${preçofinal}')