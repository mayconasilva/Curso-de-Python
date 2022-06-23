from operator import le


T = []
pares = []
for c in range(1, 5):
    num = int(input(f"Digite o {c}º valor: "))
    T.append(num)
t = tuple(T)

for p in range(0,4):
    if t[p]%2 == 0:
        pares.append(t[p])

print(f'O número 9 apareceu {t.count(9)} vezes')

if 3 not in t:
    print('O valor 3 está em nehuma posição')
else:
    print(f'O primeiro valor 3 apareceu no indice {t.index(3)}')
print(f'Os valores {pares} são pares')