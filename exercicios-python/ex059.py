#Crie um programa que leia dois valores e mostre um menu na tela: 

#[1] somar
#[2] multiplicar
#[3] maior
#[4] novos numeros
#[5] sair do programa

#Seu programa deverá realizar a operação solicitada em cada caso.


#Minha primeira resolução: DE PRIMEIRA PAPAI!! 


somar = 1
multiplicar = 2
maior = 3
novos_numeros = 4
saida = 5
usuario = None


while usuario != 5:
    try:
        print('''
            [1] somar
            [2] multiplicar
            [3] maior
            [4] novos numeros
            [5] sair do programa
            ''')

        usuario = int(input('Escolha uma das opções do Menu: '))
        if usuario not in (1, 2, 3, 4, 5):
            print('Digite apenas numeros de 1 a 5')
        if usuario == 5:
            print('Fim do programa!')
    
        if usuario == 1:
            print('O que deseja somar? ')
            usuario2 = int(input('Digite o valor do primeiro número: '))
            usuario3 = int(input('Digite o valor do segundo número: '))
            print(f'A soma entre {usuario2} + {usuario3} é = {usuario2 + usuario3}')

        if usuario == 2:
            print('O que deseja multiplicar?')
            usuario4 = int(input('Digite o primeiro número: '))
            usuario5 = int(input('Digite o segundo número: '))
            print(f'A multiplicação de {usuario4} x {usuario5} é = {usuario4 * usuario5}')

        if usuario == 3:
            print('Qual valor você deseja saber se é maior?')
            usuario6 = float(input('Digite um número qualquer: '))
            usuario7 = float(input('Digite outro número qualquer: '))
            if usuario6 > usuario7:
                print(f'O número {usuario6} é maior que o número {usuario7}')
            elif usuario6 == usuario7:
                print(f'O numero {usuario6} é igual ao número {usuario7}')
            else:
                print(f'O número {usuario6} é menor que o número {usuario7}')
    except ValueError:
        print('Digite apenas valores de 1 a 5!')
        
print('Obrigado, volte sempre!')



#Como professor demonstrou:

from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''
    [1] somar
    [2] multiplicar
    [3] maior
    [4] novos numeros
    [5] sair do programa
    ''')
    opção = int(input('Qual sua opção? '))

    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} + {n2} é {n1 + n2}')
    elif opção == 2:
        produto = n1 * n2
        print(f'A multiplicação entre {n1} x {n2} é {n1 * n2}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif opção == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente. ')
    print('=-=' * 10)
    sleep(1)
print('Fim do programa, volte sempre!')



#Sobre a primeira resolução:
#Tenho que lembrar de explicar porque no meu programa eu não tenho a opção 4 do exercício.