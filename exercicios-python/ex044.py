#Elabore um programa que calcule um valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:

# À vista dinheiro/cheque: 10% de desconto
# À vista no cartão: 5% de desconto
# Em até 2x no cartão: preço normal
# 3x ou mais no cartão: 20% de juros

#Como eu fiz:

produto = float(input('Digite o valor do produto: '))
dinheiro_cheque = produto * 10 / 100
novo_din_cheq = produto - dinheiro_cheque
a_vista = produto * 5 / 100 
novo_a_vista = produto - a_vista
cart_2x = produto / 2
cart_3x = produto * 20 / 100
novo_cart3x = produto + cart_3x

print('De qual forma você quer pagar?')
print('''[ 1 ] A vista dinheiro ou cheque // 10 por cento de desconto:
[ 2 ] A vista no cartão // 5 por cento de desconto:
[ 3 ] 2x no cartão sem juros:
[ 4 ] 3x ou mais no cartão com juros de 20 por cento:''')

opções = int(input('Sua opção: '))

if opções ==1:
    print(novo_din_cheq)
    print('Você escolheu pagar a vista ou no cheque e recebeu um desconto de 10 por cento de desconto sobre o valor do produto!')
elif opções == 2:
    print(novo_a_vista)
    print('Você escolheu pagar a vista no cartão de crédito e recebeu 5 por cento de desconto sobre o produto!')
elif opções == 3:
    print('Você escolheu pagar em até 2x no cartão e não sofreu nenhum juros e também nenhum desconto!')
    print(f'O valor fica em duas parcelas {cart_2x:.2f}')
elif opções == 4:
    cliente = int(input('Em quantas vezes você quer pagar? '))
    vezes = produto / cliente   
    parcela_3x = novo_cart3x / cliente
    print(f'Você escolheu pagar em {cliente}x no cartão, com isso você sofre um juros de 20 por cento do valor da compra!')
    print(f'O valor a ser pago é de {novo_cart3x:.2f} dividido em {cliente} parcelas de R${parcela_3x:.2f}')
else:
    print('opção invalida, tente novamente!')


    #Como professor demonstrou:

print('{:=^40}'.format('LOJAS GUANABARA'))
preço = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
[ 1 ] À vias dinheiro/ cheque
[ 2 ] À vista cartão 
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = preço - (preço * 10 / 100)
elif opção == 2:
    total = preço - (preço * 5 / 100)
elif opção == 3:
    total = preço
    parcela = total / 2
    print(f'Sua compra será parcelada em 2x de R${parcela:.2f}')
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totparc = int(input('QUantas parcelas? '))
    parcela = total / totparc
    print(f'Sua compra será parcelada em {total:.2f}x de R${totparc:.2f} com juros')
else:
    total = 0
    print('Opção inválida de pagamento. Tente novamente!')
print(f'Sua compra de {preço:.2f} vai custar R${total:.2f} no final')


#Anotações:
#Ambos os códigos resolvem o problema, porém dando destaque a forma em que 
#o professor desenvolve os cálculos diretamente nas condições enquanto eu 
#criei uma variavel para cada cálculo totalmente desnecessários.