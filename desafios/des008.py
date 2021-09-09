medida = float(input('Digite a unidade de medida em metros'))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'{medida} metros é igual a: \n {km} km \n {hm} hm \n {dam} dam \n {cm} cm \n {mm}^mm')
