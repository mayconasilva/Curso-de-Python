# [1] = Somar ; [2] = Multiplicar; [3] = Maior. [4] = Novos Números; [5] = Encerrar

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
interaão = int(input("O que você deseja fazer? \n Digite 1 para somar \n Digite 2 para Multiplicar \n Digite 3 para Maior \n Digite 4 para adicionar mais números \n Digite 5 para encerrar"))

if interaão == 1:
    print(f"A soma de {num1} + {num2} é igual a {num1 + num2}")
elif interaão == 2:
    print(f"A multiplicação entre {num1} * {num2} é igual a {num1*num2}")
elif interaão == 3:
    if num1 > num2:
        print(f"{num1} > {num2}")
    else:
        print(f"{num2} > {num1}")
elif interaão == 4:
   
    num3 = int(input("Digite um número:"))
    
    interacao = int(input("O que você deseja fazer? \n Digite 1 para somar \n Digite 2 para Multiplicar \n Digite 3 para Maior \n Digite 4 para adicionar mais números \n Digite 5 para encerrar"))
    if interacao == 1:
        print(f"A soma de {num1} + {num2} + {num3} é igual a {num1 + num2 + num3}")
    elif interacao == 2:
        print(f"A multiplicação entre {num1} * {num2} * {num3} é igual a {num1*num2*num3}")
    elif interaão == 3:
        if num1 > num2 > num3:
            print(f"{num1} > {num2} > {num3}")
        elif num2 >  num1 > num3:
           print(f"{num2} > {num1} > {num3}")
        elif num3 > num1 > num2:
            print(f"{num3} > {num1} > {num3}")
    else:
        print("O programa foi encerrado")
else:
    print("O programa foi encerrado")
