import random
import time
print('Estou pensando em um número entre 0 e 5')
print('Pensando...')
time.sleep(5)
print('Pensei')
num = random.randint(0, 5)
pensar = int(input('Quando número eu pensei?'))
time.sleep(3)
if pensar == num:
    print(f'Acertou, o número é {num}')
else:
    print(f'Errou, o número era {num}')
