a1 = int(input("Insira o primeiro termo da pa: "))
razão = int(input("Insira a razão da pa: "))
pa = []
pa.append(a1)
for c in range(0, 11):
    pa.append(pa[c] + razão)
print(f'Os 10 primeiros termos da PA é igual a {pa}')
