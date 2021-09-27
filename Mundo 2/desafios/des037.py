num = int(input("Digite um número inteiro"))
opção = int(input("Escolha [1] para binário, [2] para Octal e [3] para hexadecimal"))
if (opção == 1):
    print(f'{num} equivale a {bin(num)} em binário')
elif (opção == 2):
    print(f'{num} equivale a {oct(num)} em Octal') 
else:
    print(f'{num} equivale a {hex(num)} em hexadecimal')