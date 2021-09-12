a = int(input('Informe um número'))
b = int(input('Informe outro número'))
c = int(input('Informe mais um número'))

max = a 

if b > a and b > c:
    max = b
if c > a and c > b:
    max = c

min = a 

if b < a and b < c:
    min = b
if c < a and c > b:
    min = c

print(f'O maior é {max} e o menor é {min}' )