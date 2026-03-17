#46 Faça um programa que mostre na tela uma contagem regressiva para o estouro de
#fogos de artifício, indo de 10 até 0, com uma pausa de 1 sec entre eles.

from time import sleep

print('A contagem dos fogos do ano novo vai começar:')
for c in range(10, 0-1, -1):
    print(c)
    sleep(0.5)
print('Boom Bang Boom Bomm Bang Bom')
print('Fim da contagem!')



#47 Crie um programa que mostre na tela todos os números pares que estão no 
#intervalo entre 1 e 50.


for c in range(1+1, 50+1, 2):
    print(c)
print('Fim da contagem!')





#48 Faça um programa que calcule a soma entre todos os números impares que são 
#multiplos de três e que se encontram no intervalo de 1 a 500.



for c in range(1, 500, 2):
    print(c)
print('Fim da contagem!')


#Correção:

soma = 0
contador = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        contador += 1
    print(f'A soma dos valores è: {soma}')
print('Fim do programa')



#49 Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher
#só que agora utilizando um laço for.


tabu = input('Escolha uma tabuada qualquer: ').strip()
if not tabu:
    print('Você não digitou valor algum!')
else:
    try:
        tabus = int(tabu)
        if tabus < 0:
            print('A tabuada precisa ser de numeros positivos!')
        else:
             for c in range(1, 11, 1):
                 print(f'{tabus} X {c} = ', c * tabus)
             print('Fim da contagem')
    except ValueError:
        print('Digite apenas valores numericos!')
print('Fim do programa!')






#50 Desenvolva um programa que leia seis números inteiros e mostre a soma apenas 
#daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.




for c in range(1, 7, 1):
    usuario0 = int(input('Digite um numero par qualquer: '))
    impar = int(1)
    if usuario0 % 2 == impar:
        print('Esse numero é impar!')
    else:
        print(f'A soma entre {usuario0} + {usuario0} é igual a:', usuario0 + usuario0)
print('Fim da contagem!')








#51 Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No
#final, mostre os 10 primeiros termos dessa progressão.

conta = int(input('Digite o termo da PA:'))
conta2 = int(input('Digite a razão da PA: '))

for c in range(0, conta, conta2):
    print(c)
print('--' * 20)
print(f'Os 10 primeiros termos dessa PA são: ')
for c in range(0, conta // 2, conta2):
    print(c)

print('Fim do programa!')

#52 Fça um programa que leia um número inteiro e diga se ele é ou não um número 
#primo.

usuario = int(input('Digite um valor qualquer: ')) 
não_é_primo = usuario % 2 == 0
não_é_primo2 = usuario == 0
não_é_primo3 = usuario // 2 == 5
não_é_primo4 = (usuario + usuario) // 3 == 0
for c in range(usuario):
    if usuario == não_é_primo:
        print('Não é primo!')
    elif usuario == não_é_primo2:
        print('Não é primo!')
    elif usuario == não_é_primo3:
        print('Não é primo!')
    elif usuario == não_é_primo4:
        print('Não é primo')
    else:
        print('É primo')
print('Fim do programa!')




#53 Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, 
#desconsiderando os espaços.

#Ex: apos a sopa (sem espaços de tras pra frente)






#54 Crie um programa que leia o ano de nascimento de sete pessoas. No final,
#mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. (considere maior idade com 21 anos)


from datetime import date
hoje = date.today().year
for c in range(1, 8, 1):
    digite = int(input('Digite seu ano de nascimento: '))
    if not digite:
        print('Você não digitou valor algum!')
    else:
        try:
            if hoje - digite < 21:
                print(f'Você ainda não atingiu a maioridade! faltam {hoje - digite} anos!')
            else:
                print(f'Você já atingiu a maioridade, você tem {hoje - digite} anos!')
        except ValueError:
            print('Digite um valor numerico!')
print('Fim do contador!')






#55 Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.



peso = float(300)
for c in range(1, 6, 1):
    pessoas = float(input(('Digite seu peso: ')))
    if not pessoas:
        print('Você não digitou valor algum!')
    if pessoas < 0:
        print('Você precisa colocar pesos positivos!')
    else:
        try:
            pessoa = float(pessoas)
        except ValueError:
            print('Digite somente valores numericos!')
print('A comparação entre os pesos são: ')


print('-----')
if pessoa < 300:
    print(f'O maior peso entre todos é: {pessoa}')
print('Fim do contador!')



#56 Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final
#do programa, mostre:


#A média de idade do grupo.

#Qual é o nome do homem mais velho.

#Quantas mulheres têm menos de 20 anos.



idade = 0
for c in range(1, 5, 1):
    candidatos = int(input('Digite sua idade: '))
    candidatos2 = input('Digite seu sexo: ')
    if not candidatos or not candidatos2:
        print('Você não digitou alguns dos valores anteriores!')
    else:
        try:
            candidatos00 = int(candidatos)
            candidatos02 = str(candidatos2)
            if candidatos02 in ('masculino'):
                idade = candidatos00
            elif candidatos02 in ('feminino'):
                idade = candidatos00 
            

        except ValueError:
            print('Digite os valores pedidos!')
print('Fim do programa!')

        













