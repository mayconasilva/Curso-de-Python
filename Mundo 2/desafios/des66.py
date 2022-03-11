lista = []
s = 0

while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break
    
    lista.append(n)
    s += n
print(f"A soma dos {len(lista)} digitados é igual a {s}")
print(f"Os numeros digitados foram {lista}")