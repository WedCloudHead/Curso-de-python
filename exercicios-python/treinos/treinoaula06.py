#Primeiro código de 2026

n1 = input ('Digite um numero: ')
n2 = input ('Digite um numero: ')
s = n1 + n2
print(f'A soma vale: {s}')
print(type(n1))

#Nesse caso python esta interpretando n1 e n2 como string

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
s = n1 + n2
print(f'A soma vale {s}')
print('A soma vale', s)
print('A soma vale {}'.format(s))
print(type(s))


#Nesse caso sim o python esta reconhecendo n1 e n2 como numeros int(inteiros)

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
s = num1 + num2
print(f'A soma entre {num1} e {num2} vale: {s}')
print('A soma entre {} e {} vale: {}'.format(num1, num2, s))

