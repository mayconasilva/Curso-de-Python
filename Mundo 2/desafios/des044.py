preço = float(input("informe o prçeo do produto "))
tipodepagamento = str(input("Deseja pagar a vista ou no cartão?")).lower()
if (tipodepagamento == "a vista" or tipodepagamento == "à vista" or tipodepagamento == "á vista"):
    print(f'O preço final do produto será de R${preço - preço * 0.10:.2f}')
elif (tipodepagamento == "cartão"):
    quantidade = int(input("Deseja parcelar em quantas vezes?"))
    if (quantidade == 1):
        print(f'Pagando a vista no cartão o preço final do produto será de R${preço * preço*0.05:.2f} ')
    elif (quantidade == 2):
        print(f'Pagando no cartão 2 vezes o preço de cada parcela será de  R${preço / 2:.2f}, sendo que o preço final será o valor original')
    else:
        print(f'Haverá um acréscimo de 20% no valor final do produto, sendo que o preço dele será de R%{preço + preço*0.20:.2f}. Sendo que o valor de cada parcela será de R${(preço + preço*0.20)/quantidade:.2f}')