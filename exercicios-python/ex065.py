#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa dece perguntar ao usuário se ele quer ou não continuar a digitar valores.


#Minha resolução:


soma_num = 0
usuario = None
listas_num = []
user = 'sim'




while user != 'nao'.capitalize():
    while True:
         try:
             usuario = int(input('Digite qual número deseja adicionar: '))
             break
         except ValueError:
                print('Digite apenas numeros')

    while True:
         try:
            user = str(input('Deseja continuar? sim ou nao: ')).strip().capitalize()
            if user not in ('Sim', 'Nao'):
                 print('Digite apenas sim ou nao')
            else:
                break
         except ValueError:
              print('Digite apenas sim ou nao')

    soma_num += usuario
    listas_num.append(usuario)

media = soma_num / len(listas_num)

print(f'A media é {media:.2f}')
print(f'O maior número digitado foi: {max(listas_num)}')
print(f'O menor número digitado foi: {min(listas_num)}')



#Resolução do professor:

resp = 'S'
soma = quant = média = maior = menor = 0
while resp in 'Ss':
    núm = int(input('Digite um número: ')) 
    soma += núm
    quant += 1
    if quant == 1:
        maior = menor = núm
    else:
         if núm > maior:
              maior = núm
         if núm < menor:
              menor = núm
    resp = str(input('Quer continuar? [S/N]: ')).upper().strip()
media = soma / quant
print(f'Você digitou {quant} números e a média é {media}')
print(f'O maior número digitado foi {maior} e o menos foi {menor}')


     