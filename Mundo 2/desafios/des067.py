while True:
    n = int(input("Quer ver a tabuada de qual número: "))
    if n < 0:
        print("Você digitou um número negativo. O programa foi encerrado")
        break
    for c in range(1, 11):
        print(f'{n} * {c} = {n*c}')
print('Tenha um Bom Dia!')