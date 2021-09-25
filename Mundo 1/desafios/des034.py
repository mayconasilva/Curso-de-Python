salário = float(input('Qual o seu salário'))
if salário > 1250.00:
    print(f'Seu salário atual será de {salário + salário*0.10:.2f}')
else:
    print(f'O seu salário atual será de {salário + salário*0.15:.2f}')