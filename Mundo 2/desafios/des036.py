valor = int(input("Qual o valor do empréstimo? "))
tempo = int(input("Em quantos anos deseja parcelar os empréstimos? "))
salário = int(input("Qual o valor do seu salário mensal? "))
tempoemmeses = tempo * 12
prestações = valor / tempoemmeses

if (prestações > salário*0.30):
    print(f"Desculpe-nos, não podemos aprovar o seu empréstimos, pois o valor das prestações que seriam de {prestações:.2f} ultrapassa 30% do valor do seu salário ")
else:
    print(f"Parabéns, o seu empréstimo foi aprovado, o valor de cada prestação mensal será de R${prestações:.2f}")