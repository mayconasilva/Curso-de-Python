from time import sleep as delay
resposta = "S"
pessoa = 1

idades = []
sexos = []
contmaior = 0
contm = 0


while resposta == "S":
    idade = int(input(f"Me Informe a idade da {pessoa}ª Pessoa: "))
    sexo = str(input(f"Me infome o sexo da {pessoa}ª Pessoa: ")).upper()
    
    if idade >= 18:
        contmaior +=1
        
   
    if sexo != "M" and sexo != "F":
        sexo = str(input(f"Me infome o sexo da {pessoa}ª Pessoa: ")).upper()
        
    if idade <= 20 and sexo == "F":
        contm +=1


    resposta = str(
        input("Deseja adicionar mais um cadrasto? (S ou N) \n ")).upper()

    if resposta != "S" and resposta != "N":
        resposta = str(
            input("Deseja adicionar mais um cadrasto? (S ou N) \n ")).upper()

    pessoa += 1
    idades.append(idade)
    sexos.append(sexo)
print("=-=-=-=" * 15)
print(f"O Programa foi finalizado com {pessoa - 1} cadrastos adicionados")
print("Lendo Resultados...")
delay(1.5)
print("=-=-=-=" * 15)

print(f"De acordo com os dados informados há {contmaior} maiores de idade")
print(f'De acordo com os dados informados há {sexos.count("M")} homens cadrastados')
print(f"De acordo com os dados informados há {contm} Mulheres com idade inferior ou igual a 20 anos")

print(f"{idades} \n {sexos}")
