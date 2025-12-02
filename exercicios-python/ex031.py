#Desenvolva um programa que pergunte a distancia de uma viagem em km. 
#calcule o preço da passagem, cobrando R$0,50 por km para viagens de ate 200km e R$0,45 para viagens mais longas

#Como eu fiz:

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


#Como professor demonstrou:

distancia = float(input('Qual a distancia da sua viagem? '))
print(f'Voce esta prestes a começar uma viagem de {distancia}Km')
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f'E o preço da sua passagem sera de R${preço}')



#extra:

distancia = float(input('Qual a distancia da sua viagem? '))
print(f'Voce esta prestes a começar uma viagem de {distancia}Km')
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print(f'E o preço da sua passagem sera de R${preço}')

#essa forma simplificada da linha 36 é um metodo muito bom para problemas basicos e rapidos de se resolverem, pois segue uma estrutura bem logica, curta e organiza. 
# Como ler a linha 36: O 'preço' 'recebe' 'distancia' *0.50 'se' 'distancia' for 'menor ou igual' a 200, 'se nao' a 'distancia' sera *0.45
