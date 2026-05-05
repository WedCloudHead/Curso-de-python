#Testes:

for c in range(10):
    print(c)
print('Fim')


c = 1 
while c < 10:
    print(c)
    c += 1
print('Fim')


#-----------------------


for c in range(5):
    n = int(input('Digite um valoe: '))
print('Fim')


n = 1
while n != 0: #(Flag, condição de parada ou ponto de parada)
    n = int(input('Digite um valoe: '))
print('Fim')


#-----------------------


r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N]')).upper()
print('Fim')


#-----------------------



n = 1 
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print(f'Voce digitou {par} numeros pares e {impar} numeros impares!')

