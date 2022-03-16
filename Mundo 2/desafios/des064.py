c = 1
t = 0
n = 0

while n != 999:
    n = int(input("Digite um número (999 para parar): "))
    
    if n != 999:
        t +=n

print(f'A soma é igual a {t}')