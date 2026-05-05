#Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

#OBS: Considere cédulas de R$50, R$20, R$10 e R$1 


#Como eu fiz: 

print('Qual valor deseja sacar? (digite apenas números inteiros)')

while True:
    try:
        valor = int(input())
    except ValueError:
        print('Digite conforme sugerido')
        continue
    if valor < 0:
        print('Digite apenas valores positivos')
        continue
    
    break

qtd_50 = valor // 50
resto = valor % 50

qtd_20 = resto // 20
resto = resto % 20

qtd_10 = resto // 10
resto = resto % 10

qtd_1 = resto


print(f'O valor total retirado foram {qtd_50} notas de R$50, {qtd_20} notas de R$20, {qtd_10} notas de R$10 e {qtd_1} notas de R$1')


#Como professor demonstrou:


print('=' *30)
print('{:^30}'.format('Banco CEV'))
print('=' *30)

valor = int(input('Que valor você quer sacae? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
print('=' * 30)
print('Volte sempre ao Banco CEV! Tenha um boma dia! ')

