from random import randint

t = []

for c in range(0, 5):
    a = (randint(1, 100))
    t.append(a)
    
m = tuple(t)

print(f'Os números gerados são {m} ')
print(f'O maior valor é {max(m)}')
print(f'O menor valor é {min(m)}')

