from msilib.sequence import tables
from tabulate import tabulate

listagem = ('smartphone', 3500.43, 'carne', 22, 'açúcar', 4.2, 'pão', 3, 'café', 4.20, 'computador', 5500, 'caderno', 18.20)

table = [[f'{listagem[0]}', '{listagem[1]}' ],  [f'{listagem[2]}', '{listagem[3]}' ] [f'{listagem[4]}', '{listagem[5]}' ] [f'{listagem[6]}', '{listagem[7]}' ] [f'{listagem[8]}', '{listagem[9]}' ] [f'{listagem[10]}', '{listagem[11]}' ]]

print(tabulate(tables))