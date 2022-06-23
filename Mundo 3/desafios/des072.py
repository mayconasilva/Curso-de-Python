from time import sleep

extenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez", "onze", "doze", "treze", "quartoze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove", "vinte")

print("=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=")
print("Número por extenso")
print("=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=")

sleep(0.2)


num = int(input("Informe um número entre 0 e 20: "))

while num < 0 or num > 20:
    print("Número Inválido")
    num = int(input("Informe um número entre 0 e 20: "))

print(f"O nome por extenso de {num} é {extenso[num].capitalize()}")