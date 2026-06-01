#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
#Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.


#Primeira tentativa: 
#Consegui fazer dessa forma, porém está ao contrário quando usuário digita por extenso o programa mostra o algarismo 

extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
usuario = (input()) 
print(extenso.index(usuario))


#Segunda tentativa:
#bastava lembrar da aula 016 que ele mostra que pra acessar um índice de uma tupla usa o simbolo [] então o macete é usar extenso[usuario]


extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')


while True:
    try:
        escolha = input('Digite um número entre 0 e 20: ')
        if not escolha:
            print('Preencha o campo corretamente')
            continue
        usuario = int(escolha)
        if usuario < 0 or usuario > 20: #Também pode ser -> if usuario not in range(0, 21): ou  if not 0 <= usuario <= 20:
            print('Digite apenas números entre 0 e 20')
            continue
    except ValueError:
        print('Digite apenas números')
        continue
    
    break

print(f'O valor digitado foi: {extenso[usuario]}')


#Extra com opção de continuar ou parar:




extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
coleçao = []

while True:
    while True:
        try:
            escolha = input('Digite um número entre 0 e 20: ')
            if not escolha:
                print('Preencha o campo corretamente')
                continue
            usuario = int(escolha)
            if usuario < 0 or usuario > 20: #Também pode ser -> if usuario not in range(0, 21): ou  if not 0 <= usuario <= 20:
                print('Digite apenas números entre 0 e 20')
                continue
        except ValueError:
            print('Digite apenas números')
            continue
        break

    
    
    while True:
        print('Deseja continuar? ')
        usu = input().upper().strip()
        if not usu:
            print('O campo não pode estar vazio')
            continue
        opçao = str(usu[0])
        if opçao not in 'SN':
            print('Digite apenas [S/N]')
            continue
            
        break

    coleçao.append(extenso[usuario])
     
    if opçao == 'N':
        break
    
print(f'Os valores digitados foram{coleçao}')





#Como professor demonstrou:

cont = ('zero','um','dois','três','quatro',
        'cinco','seis','sete','oito','nove',
        'dez','onze','doze','treze','quatorze',
        'quinze','dezesseis','dezessete','dezoito',
        'dezenove','vinte')
while True:
    núm = int(input('Digite um número entre 0 e 20: '))
    if 0 <= núm <= 20:
        break
    print('Tente novamente ', end='')
print(f'Você digitou o número {cont[núm]}')


