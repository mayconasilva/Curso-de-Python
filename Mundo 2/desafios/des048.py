print("A seguir a soma de todos os números imparesmúltiplos de 3 entre 0 3 50")
num = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        num = num + c
print(f'A soma dos {cont} valores solicitados é igual a {num}')

      
    
