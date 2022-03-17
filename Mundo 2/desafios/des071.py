from time import sleep

print("=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=--=-=")
print("BANCO INTERNACIONAL ALGUMA COISA")
sleep(0.1)
print("\n CAIXA ELETRÔNICO")
print("=-=-=-=-=-=-=-=--=-=-=-=-=--=-=-=-=--=-=")
print("Carregando os seus dados. Por favor aguarde...")
sleep(0.2)
print("ATENÇÃO: No caixa apenas temos disponíveis as cédulas de R$50, R$20, R$10 e R$1")
valor = int(input("Informe o valor a ser sacado: R$"))

c50 = 0
c20 = 0
c10 = 0
c1 = 0

while valor >=50:
    valor -=50
    c50+=1
while valor >=20:
    valor -=20
    c20+=1
while valor >=10:
    valor -=10
    c10+=1
while valor >=1:
    valor -=1
    c1+=1

sleep(0.3)
print(f"Ao todos foram sacadas {c50} notas de R$50, {c20} notas de R$20, {c10} notas de R$10 e {c1} notas de R$1")

