ladoa = int(input("Informe o comprimento do lado A "))
ladob = int(input("Informe o comprimendo do lado B"))
ladoc = int(input("Informe o comprimento do lado C"))
if ladoa + ladob > ladoc or ladoc + ladoa < ladob or ladob + ladoc < ladoa:
    if (ladoa == ladob == ladoc):
        print("Um triângulo equilátero pode ser formado com esses comprimentos")
    elif (ladoa == ladob or ladob == ladoc or ladoa == ladoc):
        print("Um triângulo isósceles pode ser formado")
    else:
        print("Um triângulo escaleno pode ser formado")
else:
    print("Um triângulo não pode ser formado")