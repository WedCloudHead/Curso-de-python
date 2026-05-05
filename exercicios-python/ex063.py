#Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma sequencia de Fibonacci.

#EX: 0 > 1 > 1 > 2 > 3 > 5 > 8


#Minha resolução:  (Tive que pesquisar para saber que a formula de Fibonacci é a, b = b, a + b)


print('Essa é a sequencia dos números da famosa sequência de Fibonacci')
while True:
    try:
        num = int(input('Digite um numero inteiro qualquer para ver: '))
        break
    except ValueError:
        print('Digite apenas números')
num1 = num + 1
contador = 0
while contador < 10:
    print(num, end=' >> ')
    num, num1 = num1, num + num1
    contador += 1
    
print('Fim do programa')



#Segunda resolução:



a = 0
b = 1
while True:        
    try:
        n = int(input('Digite o termo: '))
        break
    except ValueError:
        print('Digite apenas números')

contador = 0
while contador < n:
    print(a, end=' >> ')
    a, b = b, a + b
    contador += 1

print('Fim do programa')
    




#Resolução do professor:


print('-'*30)
print('Sequencia de Fibonacci')
print('-'*30)
n = int(input('Quantos termos você quer ver? '))
t1 = 0
t2 = 1
print('~'*30)
print(f'{t1} >> {t2}', end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    print(f' >> {t3}', end=' ')
    t1 = t2
    t2 = t3
    cont += 1
print(' >> Fim ')
print('-'*30)


