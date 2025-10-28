#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto
 
#como eu fiz:

produto = float(input('digite o valor do produto para ver seu desconto: '))
desconto = ('5%')
descontoP = float(produto * 5 / 100)
valor = (produto - descontoP)
print('o desconto do produro é igual a: {} e o valor final fica: {} '.format(desconto, valor))


#como o professor demonstrou na correção:

preço = float(input('qual é o preço do produto? R$ '))
novo = preço - (preço * 5 / 100)
print('o produto que custava R${:.2f} na promoção com 5% de desconto vai custar R${:.2f} '.format(preço, novo))