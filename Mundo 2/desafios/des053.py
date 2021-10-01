palavra = str(input("Insira um palavra para verificar se ela é um palíndromo")).strip().lower().replace(' ', '')
palavrainvertida = palavra[::-1]
if palavra == palavrainvertida:
    print(f"{palavra} é um palíndromo")
else:
    print(f'{palavra} não é um palíndromo')
