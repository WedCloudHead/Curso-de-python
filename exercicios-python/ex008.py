#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros


metro = int(input('escolha uma medida em metros: '))
cem = (metro * 100)
mili = (cem * 100)
resc = (cem)
resm = (mili)

print('{} metro(s) são: {} centimetros '.format(metro, resc))
print('{} mestro(s) são: {} milimetros '.format(metro, resm))