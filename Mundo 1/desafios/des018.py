import math
graus = int(input('Informe o valor em graus'))
print(f'{graus}º possui o seno igual a {math.sin(math.radians(graus)):.2f}, o coseno igual a {math.cos(math.radians(graus)):.2f} e a tangente igual a {math.tan(math.radians(graus)):.2f}')