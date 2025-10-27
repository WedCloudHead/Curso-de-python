#escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros

#eu fiz assim:

metro = int(input('escolha uma medida em metros: '))
cem = (metro * 100)
mili = (cem * 100)
resc = (cem)
resm = (mili)

print('{} metro(s) são: {} centimetros '.format(metro, resc))
print('{} mestro(s) são: {} milimetros '.format(metro, resm))


#como o professor demonstrou na correção:


medida = float(input('Una distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm '.format(medida, cm, mm))


#extra:

#na linha 21 os parametros {:.0f} significam que apos o ponto flutuante o compilador nao deve considerar nenhum numero.

#km quilometro  
#hm hectômetro 
#dam decâmetro 
#m metro
#dm decimetro 
#cm centimetro
#mm milimetro
