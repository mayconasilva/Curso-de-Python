idade = int(input("Informe sua idade"))
if (idade >= 9 ):
    print("Você é da categoria mirim")
elif (idade < 9 and idade <= 14 ):
    print("Você é da categoria infantil")
elif (idade > 14 and idade <= 19):
    print("Você é da categoria junior")
elif ( idade >= 19 and idade == 20):
    print("Você é da categoria sênior")
else:
    print("Você é da categoria master")