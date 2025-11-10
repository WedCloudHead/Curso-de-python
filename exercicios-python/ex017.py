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


#treinando:


#1) Crie um programa que:
#sabendo o comprimento do cateto oposto e do cateto adjacente, calcule:
#.a angulo formado entre o cateto adjacente e a hipotenusa:
#.e o valor da hipotenusa:

import math
cateto = 20
catetoAdjacente = 35
anguloHiAd = hypot(math.hypot(cateto, catetoAdjacente))
print('o angulo ente o cateto adjacente {} e a hipotenusa da {:.2f} '.format(catetoAdjacente, anguloHiAd))
hipotenusa = math.hypot(cateto, catetoAdjacente)
print('o valor da hipotenusa é {:.2f} '.format(hipotenusa))


#correção)
cateto_oposto = 20
cateto_adjacente = 35
angulo_radianos = math.atan(cateto_oposto / cateto_adjacente)
angulo_graus = math.degrees(angulo_radianos)
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f'o valor da hipotenusa é {hipotenusa:.2f}')
print(f'o angulo entre o cateto adjacente ({cateto_adjacente}) e a hipotenusa é de {angulo_graus:2f}°')


#2) Altura de um prédio
#De um ponto no chão, você observa o topo de um prédio sob um ângulo de 35°.
#A distância até o prédio é de 25 metros.
#Calcule a altura do prédio (desconsidere a altura dos olhos).

import math
ângulo_predio =  float(35)
distancia_predio = int(25)
altura_predio = math.hypot(ângulo_predio, distancia_predio)
print(f'a distancia do predio {distancia_predio} metros, vezes o angulo do predio {ângulo_predio}° da o valor da altura que é: {altura_predio:.2f} metros ')

#correção

import math

angulo_predio = 35
distancia_predio = 25

#converter o angulo para radianos
angulo_rad = math.radians(angulo_predio)

#calcular a altura usando a tangente
altura_predio = math.tan(angulo_rad) * distancia_predio

print(f'a {distancia_predio} m de distancia e angulo de {angulo_predio}°')
print(f'a altura do predio é de aproximadamente {altura_predio:.2f} metros')
