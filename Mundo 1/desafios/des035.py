comprimento1 = float(input('Qual o tamanho do primeiro rato?'))
comprimento2 = float(input('Qual o tamanho do segundo rato?'))
comprimento3 = float(input('Qual o tamanho do terceiro rato?'))
if comprimento1 + comprimento2 > comprimento3 or comprimento3 + comprimento1 < comprimento2 or comprimento2 + comprimento3 < comprimento1:
    print(f'Pode formar um triângulo')
else:
    print('Não pode formar um triângulo') #1=bold. 4=underline. 7=negative
                                                        #30=w.31=r.32=g.33=y.34=b.35=r.36=b.37=gr