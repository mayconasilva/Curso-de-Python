from random import choice
from time import sleep
print("Vamos jogar pedra, papel e tesoura?")
sleep(3)
print("jokenpô")
escolha = str(input("Escolha pedra, papel ou tesoura ")).lower()
opções = ["pedra", "papel", "tesoura"]
computador = choice(opções)
if (escolha == "pedra" and computador == "tesoura" or escolha == "papel" and computador == "pedra" or escolha == "tesoura" or computador == "papel"):
    print(f'Eu escolhi {computador}')
    sleep(3)
    print("Droga, você ganhou!")
elif (computador == "pedra" and escolha == "tesoura" or computador == "papel" and escolha == "pedra" or computador == "tesoura" and escolha == "papel"):
    print(f"Eu escolhi {computador}")
    sleep(3)
    print("Viva a mim, eu sou o melhor, eu venci")
else:
    print(f'Eu escolhi {computador}')
    sleep(3)
    print("Empatamos. Vamos de novo?")
