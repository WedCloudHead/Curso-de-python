#Crie uma tupla preenchida com os 20 primeiros colocados da tabela do campeonato brasileiro de futebol(brasileirão), na ordem de colocação. Depois mostre:
#A) apenas os 5 primeiros colocados.
#B) os ultimos 4 colocados da tabela. 
#C) uma lista com os times em ordem alfabetica.
#D) em que posição na tabela está o time da Chapecoense.


#Primeira tentativa:



tabela = ('Palmeiras','Flamengo','Fluminense','São Paulo','Athletico Paranaense','Bahia','Red Bull Bragantino','Vasco da Gama Saf','Coritiba SAF','Vitória','Cruzeiro','Botafogo','Atlético Mineiro','Internacional','Santos FC','Corinthians','Grêmio','Mirassol','Remo','Chapecoense')

print('-=' * 15)
print(f'Está é a tabela do CBF {tabela}')
print('-=' * 15)
print(f' Os 5 primeiros colocados no CBF são: {tabela[0:5]} ')
print('-=' * 15)
print(f' Os ultimos 4 colocados da tabela: {tabela[-4:]} ')
print('-=' * 15)
print(f' A ordem alfabetica da tabela é {sorted(tabela)} ')
print('-=' * 15)
print(f'O time da Chapecoense se encontra na {tabela.index('Chapecoense') + 1}° posição.')
print('-=' * 15)





#Como professor demonstrou:



times = ('Palmeiras','Flamengo','Fluminense','São Paulo','Athletico Paranaense','Bahia',
         'Red Bull Bragantino','Vasco da Gama Saf','Coritiba SAF','Vitória','Cruzeiro',
         'Botafogo','Atlético Mineiro','Internacional','Santos FC','Corinthians','Grêmio',
         'Mirassol','Remo','Chapecoense')



print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros são {times[0:5]}')
print('-=' * 15)
print(f'Os 4 últimos são {times[-4:]}')
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-=' * 15)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}ª posição')
print('-=' * 15)
