num = input('Digite um número de 0 a 9999. ').strip()
print(f'{num[3]} Unidade \n {num[2]} Dezena \n {num[1]} Centena \n {num[0]} Milhar')

nu = int(num)
u = nu //1 % 10
d = nu //10 % 10
c = nu //100 % 10
m = nu //1000 % 10
print(f'{u} Unidade \n {d} Dezena \n {c} Centena \n {m} Milhar')