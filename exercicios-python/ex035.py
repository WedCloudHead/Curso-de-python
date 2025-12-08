#Desenvolva um programa que leia o comprimento de tres retas e diga ao usuario se elas podem ou não formar um triangulo 

#Como eu fiz:

from time import sleep
reta1 = int(input('Diga o comprimento da primeira reta: '))
reta2 = int(input('Diga o comprimento da segunda reta: '))
reta3 = int(input('Diga o comprimento da terceira reta: '))
print('~/~' * 10)
print('Analizando se é possivel...')
print('~/~' * 10)
sleep(2)
if reta1 + reta2 > reta3 and reta2 + reta3 > reta1 and reta1 + reta3 > reta2:
    print(f'Dado os valores {reta1}, {reta2}, {reta3} fornecidos, é possivel formar um triangulo!') 
else:
    print(f'Dado os valores {reta1}, {reta2}, {reta3} fornecidos, não é possivel formar um triangulo!') 

#Como professor demonstrou:

print('-=-'*10)
print('Analisador de Triagulos')
print('-=-'*20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo!')
else:
    print('Os segmentos acima não podem formar um triangulo!')


#Extra:

#sobre a resolução ambas resolveram o problema com maestria, tanto a minha quanto a do professor, apesar de terem tido diferenças na construção das linhas de condições, e a unica duvida que ficou foi por que o professor usou float para declarar os segmentos e não int? Acredito que seja possivel dar valores de segmentos com pontos flutuantes como 3.5 + 4.7 + 5 para analizar se é possivel ser feita a formação de um triangulo!

#No mundo dos triangulos existem algumas formações geometricas formadas por diferentes tipos de segmentos de triangulos: 
#isosceles: todos os lados iguais 
#escaleno: dois lados iguais
#equilatero: todos os lados diferentes

