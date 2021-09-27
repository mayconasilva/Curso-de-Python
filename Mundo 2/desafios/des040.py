nota1 = float(input("Me fale sua primeira nota "))
nota2 = float(input("Me informe sua segunda nota"))
média = (nota1 + nota2) / 2 
if (média >= 7):
    print(f'Parabéns, você foi aprovado com {média} pontos na média global')
elif (média >= 5 and média <= 6.9 ):
    print(f'Sinto muito, você foi para recuperação com {média} pontos na média global')
else:
    print(f'Desculpe, você foi reprovado com {média} pontos na média global')