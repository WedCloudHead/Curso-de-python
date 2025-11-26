#Escreva um programa que leia a velociadade de um carro.
#se ele ultrapassar 80k/h, mostre uma mensagem dizendo que ele foi multado.
#a multa vai custar R$7,00 por km acima do limite

carro = int(input('diga a que velocidade seu carro esta? '))
limite = int(80)

if carro > limite:
    multa01 = carro - limite
    multa02 = 7
    valor = multa01 * multa02
    print(f'Seu carro está a {carro}km/h')
    print(f'Seu carro estava acima do limite permitido na via, que é 80km/h, o valor a pagar pela multa é de: R$7,00 por km acima do limite')
    print(f'O valor a pagar é de: R${valor},00')
else:  
    print('Você pode seguir sua viagem pois seu carro esta dentro do limite de velocidade, 80km/h')

        