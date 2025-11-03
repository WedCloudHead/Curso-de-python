# escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60.00 por dia e R$ 0.15 por Km rodado.

#Como eu fiz:

KmRodado = float(input('quantos Km você percorreu com carro? '))
diasDeUso = float(input('e por quantos dias o carro foi utilizado? '))

preçoDia = float(60.00)
preçoKm = float(0.15)
totalAPagar = (diasDeUso * preçoDia) + (KmRodado * preçoKm)
print('o total a pagar pelo aluguel do carro é de: R${:.2f} '.format(totalAPagar))

#como professor demonstrou:

dias = int(input('Quantos dias alugados? '))
km = float(input('quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('o total a pagar é de R${:.2f} '.format(pago))


#O segredo de enunciados maiores é quebrar eles em pedaços e resolver em parcelas(divida para conquistar)