#Desenvolva um programa que pergunte a distancia de uma viagem em km. 
#calcule o preço da passagem, cobrando R$0,50 por km para viagens de ate 200km e R$0,45 para viagens mais longas

viagem = float(input('nessa viagem me diga quantos quilometros você percorreu? '))
minimo = float(200.00)
preçoMin = float(0.50)
preçoMax = float(0.45)
valorMin =  float(viagem * preçoMin)
valorMax = float(viagem * preçoMax)

if viagem <= minimo: 
    print(f'em viagens de ate 200km rodados o preço a pagar pela é de: {preçoMin} por km ')
    print(f'Sendo assim sua viagem fica um total de R${valorMin:.2f},00')
else:
    viagem > minimo
    print(f'em viagens acima de 200km rodados o preço a pagar é de: {preçoMax} por km ')
    print(f'Sendo assim sua viagem fica um total de R${valorMax:.2f},00')


