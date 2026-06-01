#Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla.
#Depois disso, mostre a listagem dos números gerados e também indique o menor e o maior valor que estão na tupla





#Primeira tentativa:


from random import randint 
lista = [] 
sortidos = () 
for n in range(5): 
    numeros = randint(0, 5) 
    lista.append(numeros) 
    sortidos = lista 


print(f'A lista dos números aleatórios é: {sortidos}') 
print(f'O menor número da lista é: {min(sortidos)} ') 
print(f'O maior número da lista é: {max(sortidos)}')




#Segunda tentativa: 


from random import randint 
lista = [] 
for n in range(5): 
    numeros = randint(0, 5) 
    lista.append(numeros) 
    tuple(lista) = lista 


print(f'A lista dos números aleatórios é: {lista}') 
print(f'O menor número da lista é: {min(lista)} ') 
print(f'O maior número da lista é: {max(lista)}')




#Terceira tentativa:


from random import randint

lista = []

for n in range(5):
    numeros = randint(0, 5)
    lista.append(numeros)
    

sortidos = tuple(lista)

print(f'A lista dos números aleatórios é: {sortidos}')
print(f'O menor número da lista é: {min(sortidos)} ')
print(f'O maior número da lista é: {max(sortidos)}')



 #Como professor demonstrou: 

from random import randint

numeros = randint((1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

print(f'Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n}', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')