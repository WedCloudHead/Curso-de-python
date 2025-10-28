#faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

#eu fiz assim:

num = int(input('digite um numero qualquer:'))
tab = (num * 1, num * 2, num * 3, num * 4, num * 5, num * 6, num * 7, num * 8, num * 9, num * 10)
res = ('a tabuada de {} é: {} '.format(num, tab))
print(res)

#como o professor demonstrou na correção:

num = int(input('digite um numero para ver sua tabuada: '))
print('-' * 12)
print('{} x {:2} = {} '.format(num, 1, num*1))
print('{} x {:2} = {} '.format(num, 2, num*2))
print('{} x {:2} = {} '.format(num, 3, num*3))
print('{} x {:2} = {} '.format(num, 4, num*4))
print('{} x {:2} = {} '.format(num, 5, num*5))
print('{} x {:2} = {} '.format(num, 6, num*6))
print('{} x {:2} = {} '.format(num, 7, num*7))
print('{} x {:2} = {} '.format(num, 8, num*8))
print('{} x {:2} = {} '.format(num, 9, num*9))
print('{} x {:2} = {} '.format(num, 10, num*10))
print('-' * 12)

#extra: 

#essa forma de resolver o problema diretamente no print quando é um problema mais simples é muito eficiente na hora de poupar tempo e um programa que tenha muitas linhas

#os parametros :2 servem para mostrar o compilador que ele deve ler os numeros escohlidos dentro {} que estao com :2 como se estivesse sempre considerando dois digitos; 
#o que era assim:     fica assim:

#33 x 1 = 33          33 x  1 = 33 
#33 x 2 = 66          33 x  2 = 66    
#33 x 3 = 99          33 x  3 = 99
#33 x 4 = 132         33 x  4 = 132
#33 x 5 = 165         33 x  5 = 165
#33 x 6 = 198         33 x  6 = 198 
#33 x 7 = 231         33 x  7 = 231 
#33 x 8 = 264         33 x  8 = 264  
#33 x 9 = 297         33 x  9 = 297 
#33 x 10 = 330        33 x 10 = 330 
                               
#mantendo uma certa ordem dentre as colunas de numeros            


#o parametro print('-' * 12) nas linhas 13 e 24 é um diferencial que o python tem de pegar esses traços: - e multiplicar eles 12 vezes, poderia ser 20, 30, qualquer valor 