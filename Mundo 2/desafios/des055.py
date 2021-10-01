pesos = []
for c in range(1, 6):
    peso = float(input(f"Informe o peso da {c}ª pessoa"))
    pesos.append(peso)
print(f'O maior peso foi {max(pesos)}kg e o menor foi de {min(pesos)}kg')
