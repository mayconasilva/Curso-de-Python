name = input('Qual o seu nome completo?').strip()
name1 = name.split()
#Há a necessidade do nome ter 4 palavras sem o uso das condições e repetições    
nameone = name1[0]
nametwo = name1[1]
nametres = name1[2]
nametfor = name1[3]
nome = nameone + nametwo + nametres + nametfor

print(f'O seu nome é {name.upper()} com todas as letras maiúsculas e é {name.lower()} com todas as letras minúsculas \n {name} possui {len(nome)} letras \n O primeiro nome possui {len(nameone)} Letras')