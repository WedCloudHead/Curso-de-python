#crie um programa que leia quanto tem na carteira e mostre quantos dolares ela pode comprar 
#(considere: uss1,00 = rs3,27)

carteira = float(input('digite o valor que esta na sua carteira: '))
real = float(3.27)
compraDeDolar = float(carteira / real)
print(compraDeDolar)