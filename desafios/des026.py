name = input('Digete um nome com a letra A')
nome1 = name.lower().count('a')
print(f'A letra "a" aparece {name.lower().count("a")} vezes, a letra a aparece pela primeira vez no {name.lower().find("a")} e pela última vez no {name.lower().rfind("a")}')