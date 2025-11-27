#Escreva um programa que leia a velociadade de um carro.
#se ele ultrapassar 80k/h, mostre uma mensagem dizendo que ele foi multado.
#a multa vai custar R$7,00 por km acima do limite

#Como eu fiz:

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


#Como o professor demonstrou:

velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print(f'MULTADO! Você excedeu o limite permitido que é de 80kmqh')
    multa = (velocidade - 80) * 7
    print(f'Você deve pagar uma multa de R${multa:.2f}')
print('Tenha um bom dia! Dirija com segurança!')





#Extra:
#linha 24 até essa aula eu não sabia que podia misturar na declaração, uma declaração em string com numerica como está: velocidade > 80 e os demais exercicios estarao todos assim eu primeiro declaro que uma estring significa um numero e depois faço uma declaraçao calculando uma declaraçao com outra.

#o metodo de pegar e partir o trabalho ou problema em partes para resolver separadamente cada topico é tambem chamado de refinamento sucessivo dentroda programação. o famoso "dividir para conquistar"