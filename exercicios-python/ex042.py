#Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

# Equilátero: todos os lados iguais
# Isósceles: dois lados iguais 
# Escaleno: todos os lados diferentes


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
    print(f'Dado os valores {reta1}, {reta2}, {reta3} fornecidos, é possivel formar um triangulo!', end='') 
    if reta1 == reta2 == reta3:
        print('É Equilátero!')
    elif reta1 == reta2 > reta3 or reta2 == reta3 > reta1 or reta1 == reta3 > reta2:
        print('É Isósceles!')
    else: 
        reta1 != reta2 > reta3 or reta2 != reta3 > reta1 or reta1 != reta3 > reta2
        print('É Escaleno!')
else:
    print(f'Dado os valores {reta1}, {reta2}, {reta3} fornecidos, não é possivel formar um triangulo!') 


#complementando (mantive aqui somente pra deixar registrado o erro!): 

if reta1 == reta2 == reta3:
    print(f'Dado os valores {reta1}, {reta2}, {reta3} fornecidos, é formado um triângulo Equilátero')
elif reta1 == reta2 > reta3 or reta2 == reta3 > reta1 or reta1 == reta3 > reta2:
    print(f'Dado os valores {reta1}, {reta2}, {reta3} fornecidos, é formado um triângulo Isósceles')
elif reta1 != reta2 > reta3 or reta2 != reta3 > reta1 or reta1 != reta3 > reta2:
    print(f'Dado os valores {reta1}, {reta2}, {reta3} fornecidos, é formado um triângulo Escaleno')
else: 
    print(f'Dado os valores {reta1}, {reta2}, {reta3} fornecidos, não é possivel formar um triangulo!') 



#Correção:
#Não consegui resolver o problema do qual o python entenda que escaleno é quando uma reta diferente de outra reta seja maior que outra reta desde quê as duas somas de reta sempre dê maior que a terceira reta, e mesmo eu deixando isso claro na linha 30:
#reta1 != reta2 > reta3 or reta2 != reta3 > reta1 or reta1 != reta3 > reta2
#onde uma reta diferente de outra sempre tem que dar um valor maior que a terceira reta. quando colocado em teste o valor 1, 9, 8 o programa deve apontar que não é possivel montar um escaleno pois 1 + 8 não da maior que 9.
#e o programa aponta que esse resultado dá escaleno.

#Começo da explicação do Professor + correção:
#Após ouvir o começo da explicação do professor eu já compreendi qual foi meu erro de lógica para resolver o problema, eu estava tratando a possibilidade de existir ou não existir um triangulo separadamente com a as condições de que se existir o triângulo o que ele será, sendo que se for possível o triângulo automaticamente tem que ser mostrado o que ele é!


#Como professor demonstrou:


r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar um triangulo!', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isósceles!')
else:
    print('Os segmentos acima não podem formar um triangulo!')

#Sobre a aula:

#Depois de entender melhor sobre as condições aninhadas eu entendi completamente a lógica por trás de criar condições dentro de condições. 
#Todos os dois códigos resolvem o problema e dando foco para a o código do professor que encurta as linhas de código utilizando lógica pura!