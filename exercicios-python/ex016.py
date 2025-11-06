#crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira.

#Ex: digite um numero: 6.127; O numero 6.127 tem a parte interia 6.


#Como eu fiz:

from math import trunc
num = float(input('Digite um numero real: '))
inteiro = trunc(num)
print('O numero inteiro de {} é {} '.format(num, inteiro))


#Como professor demonstrou:

#1)
from math import trunc
num = float(input('Digite um valor: '))
print('O valor foi {} e a sua porção inteira é {} '.format(num, trunc(num)))

#2)
num = float(input('Digite um valor: '))
print('O valor digitado foi {} e a sua porção inteira é {} '.format(num, int(num)))


#a primeira forma esta de acordo com o jeito que eu fiz, a segunda forma tem a ver com uma maneira de tambem resolver esse mesmo problema sem precisar importar da biblioteca algo, utilizando apenas o int que é o parametro python que busca um numero inteiro qualquer ou seja ele ira tranformar o numero pedido em um numero inteiro.

