n = 0
lista = []
user = 0
total = 0

while user != "N":
    n = int(input("Digite um número"))
    lista.append(n)
    total += n
    user = str(input("Quer continuar? (S/N) ")).upper().strip()[0]

maior = max(lista)
menor = min(lista)

print(f'Ao todo você digitou {len(lista)} números; \n A média entre os números é igual a {total/len(lista)}. \n O maior número escrito é o {maior} e o menor número escrito é o {menor}')
