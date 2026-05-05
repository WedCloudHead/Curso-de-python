#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido quando o número solicitado for negativo.


#Primeira forma, forma burra:

usuario = 0

while usuario >= 0:
    try:
        usuario = int(input('Digite qualquer número para ver sua tabuada: '))
    except ValueError:
        print('Digite apenas números')
    if usuario < 0:
        print('Obrigado')
    else:
        print(f'''
        1 x {usuario} = {1 * usuario}
        2 x {usuario} = {2 * usuario}
        3 x {usuario} = {3 * usuario}
        4 x {usuario} = {4 * usuario}
        5 x {usuario} = {5 * usuario}
        6 x {usuario} = {6 * usuario}
        7 x {usuario} = {7 * usuario}
        8 x {usuario} = {8 * usuario}  
        9 x {usuario} = {9 * usuario}
        10 x {usuario} = {10 * usuario}
                ''')
        print('Para parar basta digitar qualquer valor negativo!')
print('Fim do programa')


#Segunda forma, forma inteligente, muito parecida com a do professor, porém com validação de erro:



while True:
    while True:
        try:
            print('Para parar digite qualquer valor negativo')
            usuario = int(input('Digite um número para ver sua tabuada: '))   
            break
        except ValueError:
            print('Digite apenas números')
    if usuario < 0:
        break       
    else:
        for c in range(1,11):
            print(f'{usuario} x {c} = {usuario * c}')

print('Fim do programa')


#Como professor demonstrou:

while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-' * 30)
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
    print('-' * 30)
    
print('PROGRAMA ENCERRADO. Volte sempre!')
