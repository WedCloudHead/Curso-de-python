#Exercicios de trigonometria:

#1)Aplicações diretas (básico)
#Calcular seno, cosseno e tangente de vários ângulos

#Peça ao usuário para digitar vários ângulos separados por vírgula
#(ex: 30, 45, 60, 90) e mostre uma tabela com seno, cosseno e tangente de cada um.


import math
usuario = float(input('Digite varios angulos separados por virgulas: '))

tabela = [math.sin(usuario), math.cos(usuario), math.tan(usuario)]

print(f'o seno, cosseno e a tangente de {usuario} é igual a {tabela}')


