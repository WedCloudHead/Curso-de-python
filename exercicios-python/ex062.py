#Melhore o desafio 061, perguntando para o usuario se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.


#Minha resolução:


while True:
    try:
        termo = int(input('Digite o primeiro termo da PA: '))
        razao = int(input('Digite a razão da PA: '))
        break
    except ValueError:
        print('Digite apenas valores numericos!')

contador = 0      
print('Os 10 primeiros termos da PA: ')
while contador < 10:
    print(termo, end=', ')
    termo += razao
    contador += 1


soma_final = 0
usuario = 1
while usuario != 0:
    while True:
        try:
            print('Se quiser encerrar basta precionar a tecla [0]') 
            usuario = int(input('Deseja ver mais termos? '))   
            break
        except ValueError:
            print('Digite apenas valores númericos')
    total = usuario + contador
    soma_final += usuario
    while contador < total:
        print(termo, end=', ')
        termo += razao
        contador += 1

print(f'Ao todo teve o total de {soma_final} termos a mais')          
print('Fim do programa!')



#Resolução do professor:


print('Gerador de PA')
print('-=' * 15)
primeiro = int(input('Primeiro Termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end=' -> ')
        termo += razão
        cont += 1
    print('PAUSA')

    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos mostrados.')
print('FIM')

