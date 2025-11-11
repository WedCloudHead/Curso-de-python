#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.


#1)
import math
angulo = float(input('Digite o angulo que voce deseja: '))
seno = math.sin(math.radians(angulo))
print('o angulo de {} tem o seno de {:.2f} '.format(angulo, seno))
cosseno = math.cos(math.radians(angulo))
print('o angulo de {} tem o cosseno de {:.2f} '.format(angulo, cosseno))
tangente = math.tan(math.radians(angulo))
print('o angulo de {} tem a tangente de {:.2f} '.format(angulo, tangente))


#2)
from math import sin, cos, tan
angulo = float(input('Digite o angulo que voce deseja: '))
seno = sin(math.radians(angulo))
print('o angulo de {} tem o seno de {:.2f} '.format(angulo, seno))
cosseno = cos(math.radians(angulo))
print('o angulo de {} tem o cosseno de {:.2f} '.format(angulo, cosseno))
tangente = tan(math.radians(angulo))
print('o angulo de {} tem a tangente de {:.2f} '.format(angulo, tangente))






#lembrando que as diferenças entre ex 1 e ex 2 são apenas os imports diferentes das bibliotecas math de python, sendo o ex 2 o import mais especifico e simplificado



#Importante;
#ao usar sin(seno), cos(cosseno) e tan(tangente) os imports de acordo com o manual em python.org (https://docs.python.org/3/library/math.html) diz que é preciso converter angulo x de graus para radianos como demonstrado na linha 7, 9 e 11 


#qualquer duvida posterior basta rever: https://youtu.be/9GvsphwW26k?si=suDNylrlmvMe8UZG



#treinando:


#1) Crie um programa que:
#peça um angulo em graus
#mostre o mesmo angulp em radianos
#e o inverso: um valor em radianos converetido para graus

import math
angulo = float(input('Digite o valor de um angulo: '))
graus = sin(math.degrees(angulo))
print('o valor em graus da {:.2f} covertido para angulo da {} '.format(graus, angulo))
radianos = sin(math.radians(angulo))
print('o valor de radiano da {:.2f} convertido para angulo da {} '.format(radianos, angulo))
inverso = sin(math.radians(graus))
print('os valor de radiano da {:.2f} convertido para graus da {:.2f} '.format(inverso, graus))


#correção)
import math
angulo_graus = float(input('Digite um angulo em graus: '))
angulo_radianos = math.radians(angulo_graus)
print(f'{angulo_graus}° equivalem a {angulo_radianos:.4f} radianos')

radianos = float(input('digite um angulo em radianos: '))
graus = math.degrees(radianos)
print(f'{radianos:.4f} radianos equivalem a {graus:.2f}°')





