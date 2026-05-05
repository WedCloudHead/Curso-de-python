#Faça um programa que leia um numero qualquer e mostre o seu fatorial.

#Ex: 5! = 5x4x3x2x1 = 120


#Como fiz minha primeira resolução: DE PRIMEIRA PAPAI!!

from math import factorial

usuario = None
print('Esse é o programa de calculo de fatorial!')
while usuario != 0:
    try:
        usuario = int(input('Digite um número qualquer para ver seu fatorial: '))
        if usuario == 0:
            print('Fim do programa ')
        else:
            usuario2 = factorial(usuario)
            print('--'*20)
            print(f'O valor fatorial do numero {usuario} é {usuario2}')
            print('--'*20)
            print('Deseja ver outro valor ou para encerrar o programa pressione 0: ')
    except ValueError:
        print('Digite apenas valores numericos!')

print('Volte sempre!')
    


#Como professor demonstrou:

#Primeira resolução:
from math import factorial
n = int(input('Digite um número para calcular seu fatorial: '))
f = factorial(n)
print(f'O fatorial de {n} é {f}')



#Segunda resolução:
n = int(input('Digite um número para calcular seu fatorial: '))
c = n 
f = 1
print(f'Calculando {n}! ' , end='' )
while c > 0:
    print(f'{c}' , end='' )
    print(' x ' if c > 1 else ' = ' , end='' )
    f *= c
    c -= 1
print(f'{f}')


