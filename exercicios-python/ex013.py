#faça um algoritmo que leia o salario e mostre seu novo salario, com 15% de aumento

#como eu fiz:

salario = float(input('digite o valor do salario para ver seu aumento: '))
porcentagem = ('15%')
aumento = float( salario * 15 / 100)
soma = float(salario + aumento)
valorFinal = float(soma)
print('o aumento é de {} e seu salario final fica: {} '.format(porcentagem, valorFinal))

#como o professor demonstrou na correção:

salário = float(input('qual é o salario do funcionario? R$ '))
novo = salário + (salário * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com aumento de 15%, passa a receber R${:.2f} '.format(salário, novo))
