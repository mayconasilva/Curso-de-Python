Número = 0
numeros = []
for c in range(1, 6):
    num = int(input(f"Digite o {c}º número: "))
    Número += num
    numeros.append(num)
    print(f'A tabuada da multiplicação de {num} é igual a: ')
    for a in range(1, 11):
        print(f'  \n {num} * {a} = {num * a}')
    print(f"A soma de todos os números informados é igual a  igual a {Número}")
    print(f'O maior valor é igual a {max(numeros)} e o menor valor é igual a {min(numeros)}')

