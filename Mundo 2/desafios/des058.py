import random as ge

resposta = ge.randint(1, 11)

jogador = int(input("Olá jogador, preparado para mais uma rodada? Adivinhe em qual número eu pensei?"))

c = 0
print(resposta)
while jogador != resposta:

    c += 1
    jogador = int(input(f"Fraco! Você achou mesmo que a resposta certa seria {jogador}? Ha Ga Ha. Falhou miseravelmente pela {c}ª vez. Tente novamente"))
print(f"Droga. Não foi dessa vez. Você acertou na {c}ª tentativa.")