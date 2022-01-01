one = int(input("Primeiro Termo: "))
razão = int(input("Razão: "))

termo = one
c = 1

while c <=10:
    print(f'{termo} => ', end="")
    termo += razão
    c += 1
    