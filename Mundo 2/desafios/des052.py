number = int(input("Insira um número e eu irei dizer se ele é primo ou não: "))
a = 0
for c in range(1, 100):
    if number % c == 0:
        a = a + 1
if a == 2:
    print("É um número primo")
else:
    print("Não é um número primo")
print(a)
