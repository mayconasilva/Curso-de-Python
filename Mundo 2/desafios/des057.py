sexo = str(input("Qual o seu sexo? (M ou F)"))
while sexo != "M" and sexo != "F":
    sexo = str(input("Por favor, digite corretamente qual o seu sexo. M ou F?"))
if sexo  == "M":
    ind = "Masculino"
else:
    ind = "Feminino"
print(f"Olá individuo do sexo {ind}")
print(f"Lembre-se que sexo é difente de gênero")