#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa.


#Como eu fiz:

#não fiz

#como professor demonstrou:

#1)
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f} '.format(hi))


#2)
import math 
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(co, ca)
print('A hipotenusa vai medir {:.2f} '.format(hi))


#3)
from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f} '.format(hi))


#Explicação:

#1) no primeiro exemplo o problema é resolvido sem a adição do modulo importado da biblioteca math fazendo com que o programador tenha que executar todo o comando linha por linha do calculo necessario para que o compilador python execute

#2) no segundo exemplo é mostrado o import math que é a importação completa da biblioteca math e na linha 21 ja é possivel notar que não é mais preciso digitar linha por linha, comando por comando para que o compilador python entenda o que é preciso para calcular a hipotenusa; o proprio comando: math.hypot(co, ca) lembrando que co e ca são referentes ao valores que eu escolhi, o compilador ja sabe que hypot é a hipotenusa e ele ja sabe como calcular ela.

#3) no exemplo 3 é simplismente aquela forma mais simples e eficaz de importar somente o hypot da biblioteca math 