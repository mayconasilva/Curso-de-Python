from time import sleep

resposta = "S"

preço_final = 0
valor_1000 = 0

valor_barato = 0
nome_barato = ''


print("=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=")
print("SUPER LOJA BARATA MASTER PYTHON")
print("=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=")

while resposta == "S":
    nome_produto = str(input("Informe o nome do Produto: ")).strip()
    preço_produto = float(input("Informe o preço do Produto: (Utilize o '.' ao invés da ',') "))
    resposta = str(input("Deseja adicionar mais um produto? (S ou N)")).capitalize()
    
    preço_final += preço_produto
    
    if preço_produto >= 1000.0:
        valor_1000 += 1
        
    
    if resposta != "S" and resposta != "N":
        print("Resposta inválida! Por favor, digite novamente")
        resposta = str(input("Deseja adicionar mais um produto? (S ou N)")).capitalize()
        
    if valor_barato == 0:
        valor_barato = preço_produto
        nome_barato = nome_produto
    else:
        if valor_barato > preço_produto:
            valor_barato = preço_produto
            nome_barato = nome_produto

print("=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
print("Lendo os dados informados...")
sleep(0.7)
print("Por favor aguarde...")
sleep(1.3)
print(f'Segundos os dados informados, o valor total da compra será de R${preço_final:.2f} \n Ao todo, {valor_1000} produtos custaram mais de R$1000.00 \n O produto mais barato foi o {nome_barato} com o preço de R${valor_barato:.2f} ')
print("=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
