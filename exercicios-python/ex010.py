#crie um programa que leia quanto tem na carteira e mostre quantos dolares ela pode comprar 
#(considere: uss1,00 = rs3,27)

#como eu fiz:

carteira = float(input('digite o valor que esta na sua carteira: '))
dolar = float(1.00)
real = float(3.27)
compraDeDolar = float(carteira / real)
print('voce pode comprar com {} reais, {:.2f} dolares '.format(carteira, compraDeDolar))


#como o professor demonstrou na correção:

real = float(input('quanto de dinheiro voce tem na carteira? R$ '))
dolares = real / 3.27 
print('com R${:.2f} voce pode comprar US{:.2f} '.format(real, dolares))



#extra:

#o maior problema na resolução de alguns exercicios carece de um conhecimento em matematica somente, a minha execuçao do exercicio esta correta mas pode se notar que foi algo muito mais advindo de um acerto forçado do que controlado.