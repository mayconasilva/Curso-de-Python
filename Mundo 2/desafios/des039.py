from datetime import date
resposta = str(input("Você já se alistou no exército?(sim ou não) "))
if (resposta.lower() == "sim"):
    print("Parabéns por servir do seu país")
    
elif (resposta.lower() == "não"):
    data = date.today().year
    ano = int(input("Me informe seu ano de nascimento"))
    idade = data - ano
    if (idade == 18):
        print("Você precisa se alistar")
    elif (idade < 18):
        print(f'Daqui {18-idade} ano(s) você precisará se alistar')
    else:
        print(f"Você já passou da hora de se alistar. Você devia ter se alistado a {idade - 18} ano(s) ")
    
else:
    print("Só aceitamos sim ou não como resposta.")
