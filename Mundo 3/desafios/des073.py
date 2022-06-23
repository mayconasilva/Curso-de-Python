#Tupla referente a tabela do Brasileirão 2022 na data de 19/03/2022, antes de começar de fato o campeonato
table_brasileirão = ("América - MG", "Atlético - PR", "Atlético - GO", "Atlético - MG", "Avaí", "Botafogo", "Ceára SC", "Corinthias", "Coritiba", "Cuiabá", "Flamengo", "Fluminense", "Fortaleza", "Goiás", "Internacional", "Juventude", "Palmeiras", "Bragantino", "Santos", "São Paulo")

ordem_alfabetica = sorted(table_brasileirão)


print(f"O 5 primeiros colocados são {table_brasileirão[0:5]}")
print(f"Os 4 últimos colocados são {table_brasileirão[16::]}")
print(f"A lista em ordem alfabética dos times é: {ordem_alfabetica}")
print(f"O time Flamengo está na posição {table_brasileirão.index('Flamengo') + 1}") # No desafio o time a ser mostrado seria o Chapecoense, mas ele não está na série B