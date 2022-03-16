import random

while True:
    jogador = str(input("Ímpar ou Par:"))
    n = random.randint(0, 10)
    print(n)
    if n%2 == 0:
        if jogador.lower() == "par":
            print("Você ganhou") 
        else:
            print("Você perdeu!")
            break
    else:
        if jogador.lower() == "Ímpar":
            print("Você ganhou")
        else:
            print('Você Perdeu!')
            break
        
print("O programa foi encerrado. Tenha um Bom Dia!")