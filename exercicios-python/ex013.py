#faça um algoritmo que leia o salario e mostre seu novo salario, com 15% de aumento


salario = float(input('digite o valor do salario para ver seu aumento: '))
porcentagem = ('15%')
aumento = float( salario * 15 / 100)
soma = float(salario + aumento)
valorFinal = float(soma)
print('o aumento de {} e seu salario final fica: {} '.format(porcentagem, valorFinal))