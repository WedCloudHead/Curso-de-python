#faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu antecessor.


#como eu fiz:

n = int(input('tap any int number: '))

print('seu antecessor é:', n - 1)
print('seu sucessor é:', n + 1)


#como o professor demonstrou na correção:

n = int(input('digite um numero: '))
a = n - 1 
s = n + 1
print('Analizando o valor {}, seu antecessor é {}, e o seu sucessor é {} '.format(n, a, s))

#como o pedido do desafio é um pedido simples de apenas retornar um antecessor e um sucessor simplismente existe uma forma mais compacta de se resolver tambem que é assim:

n = int(input('digite um numero: '))
print('Analizando o valor {}, seu antecessor é {}, e o seu sucessor é {} '.format(n, (n-1), (n+1)))

#sendo a unica diferença a exclusao das variaveis a = n - 1 por (n-1) e a = n + 1 por (n+1)