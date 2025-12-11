#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.

#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do sálario ou então o empréstimo será negado.

#como eu  fiz:

casa = float(input('Qual o valor da casa que você ira comprar? '))
salário = float(input('Qual valor do seu salário mensal? '))
tempo = int(input('Em quanto tempo você pretende quitar a casa? '))
minimo = salário * 30 / 100


if casa / tempo > salário * 30 / 100:
    print(f'Infelizmente voce não pode fazer este empréstimo pois a mensalidade de R${minimo:.2f} é maior que 30% do valor total do seu salário')
else:
    print(f'voce pode financiar essa casa pois o valor da mensalidade de R${minimo:.2f} é menor ou igual a 30% do seu sálario: R${salário:.2f}')

#como professor demonstrou:

casa = float(input('Valor da casa: R$'))
salário = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestação = casa / (anos + 12)
mínimo = salário * 30 / 100
print(f'Para uma casa de R${casa:.2f} em {anos:.2f} anos')
print(f'a prestação será de R$ {prestação:.2f}')
if prestação <= mínimo:
    print('Emprestimo pode ser CONSEDIDO!')
else:
    print('Emprestimo NEGADO!')
    

#extra:

#os dois codigos entragam a resolução do problema, porem é importante notar a forma lógica e bem organizada de ambos, o meu formato aparenta estar mais corrido, um formato sem muito detalhes, enquanto do professor mais explicativo, cada declaração bem colocada, bem exemplificado!