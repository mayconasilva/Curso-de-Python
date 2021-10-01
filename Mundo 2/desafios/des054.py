from datetime import date
data = date.today().year
pessoas = 0
nascimento = []
for c in range(1, 7):
    ano = int(input("Insira o ano de nascimento: "))
    if int(data) - ano >= 18:
        pessoas = pessoas + 1
        nascimento.append(ano)

print(f"As {pessoas} que nasceram nos anos de {nascimento} já estão na maioridade")