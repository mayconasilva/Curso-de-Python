a = 0
for c in range(0, 6):
    num = int(input("Digite um número inteiro: "))
    if num % 2 == 0:
        a = a + num
print(f"A soma dos números pares informados é igual  {a}")
