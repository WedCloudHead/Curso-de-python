#Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final mostre:

#A) Quantos vezes apareceu o valor 9
#B) Em qual posição foi digitado o primeiro valor 3
#C) Quais foram os números pares 
#(se for digitado um valor inexistente o programa deve mostrar)



#Primeira tentativa:


lista = []
pares = []

for _ in range(4):
    while True:
        try:
            valores = int(input('Digite 4 números: '))
        except ValueError:
            print('Preencha o campo corretamente')
            continue
        break
    lista.append(valores)
    if valores % 2 == 0:
        pares.append(valores)

    

print(f'Foram digitados os valores: {lista} ')


if not 9 in lista:
    print('Não foi digitado o valor 9')
else:
    print(f'Tiveram {lista.count(9)} números 9 digitados')

if not 3 in lista:
    print('Não foi digitado o valor 3 ')
else:
    print(f'O valor 3 aparece a primeira vez na {lista.index(3) + 1}° posição da lista')

if not pares:
    print('Não foram digitados valores pares')
else:
    print(f'Os valores pares digitados foram {pares}')

print('Fim do programa')


#Segunda tentativa:


lista = []
pares = []

for _ in range(4):
    while True:
        try:
            valores = int(input('Digite 4 números: '))
        except ValueError:
            print('Preencha o campo corretamente')
            continue
        break
    lista.append(valores)
    if valores % 2 == 0:
        pares.append(valores)

    
tupla = tuple(lista)

print(f'Foram digitados os valores: {tupla} ')


if 9 not in tupla:
    print('Não foi digitado o valor 9')
else:
    print(f'Tiveram {tupla.count(9)} números 9 digitados')

if not 3 in tupla:
    print('Não foi digitado o valor 3 ')
else:
    print(f'O valor 3 aparece a primeira vez na {tupla.index(3) + 1}° posição da tupla')

if not pares:
    print('Não foram digitados valores pares')
else:
    print(f'Os valores pares digitados foram {pares}')

print('Fim do programa')

   
#Como o professor demonstrou: 

num = (int(input('Digite um número: ')), int(input('Digite outro número: ')), int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
print(f'Você digitou os valores: {num}')

print(f'O valor 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O valor 3 apareceu {num.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
for n in num:
    if n % 2 == 0:
        print(n, end='')
