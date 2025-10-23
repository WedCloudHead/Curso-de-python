#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto


produto = float(input('digite o valor do produto para ver seu desconto: '))
desconto = ('5%')
descontoP = float(produto * 5 / 100)
valor = (produto - descontoP)
print('o desconto do produro é igual a: {} e o valor final fica: {} '.format(desconto, valor))