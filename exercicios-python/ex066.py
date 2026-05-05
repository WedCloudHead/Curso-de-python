#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles. (desconsiderando a flag)

#Forma 1, utilizando lista 

listas_total = [] 
usuario = None 
print('Esse é o guarda números!') 
while usuario != 999: 
    print('Caso deseje encerrar digite: (999)') 
    print('Adicione números na lista!') 
    try: 
        usuario = int(input('Digite o número que deseja adicionar: ')) 
        if usuario != 999: 
            listas_total.append(usuario) 
    except ValueError: 
        print('Digite apenas números') 
        
print(f'O total de númeoros adicionados na lista foram: {listas_total}') 
print(f'Ao todo foram digitados o total de {len(listas_total)} números') 
print(f'A soma dos valores dentro da lista é: {sum(listas_total)}')


#Forma 2, utilizando variável 


soma_final = 0
soma = 0
usuario = None

while usuario != 999:
    while True:
        try:
            usuario = int(input('Digite um número qualquer (999 para parar): '))
            if usuario != 999:
                soma += 1
                soma_final += usuario
            else:
                break
        except ValueError:
            print('Digite apenas números')

print(f'Ao todo foram digitados {soma} números e a soma entre eles foi {soma_final}')


#Forma 2, utilizando variável com apenas 1 while


soma = contador = 0
usuario = None

while usuario != 999:
    try:
        usuario = int(input('Digite um número qualquer (999 para parar): '))
        if usuario == 999:
            break
        else:
            contador += 1
            soma += usuario
    except ValueError:
        print('Digite apenas números')

print(f'Ao todo foram digitados {contador} números e a soma entre eles foi {soma}')


#Ambas três formas funcionam!!!


#Como professor demonstrou: 

soma = cont = 0 
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    soma += num
    cont += 1
print(f'A soma dos {cont} valores foi {soma}!')


