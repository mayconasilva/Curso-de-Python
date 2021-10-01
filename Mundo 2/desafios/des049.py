num = int(input("Insira o número do qual deseja receber a tabuada da multiplicação: "))
multiplicador = 1
for c in range(1, 11):
    print(f'{num} X {c} = {num*c}')