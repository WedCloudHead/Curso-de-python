#22 Crie um programa que leia o nome completo de uma pessoa e mostre:

# o nome com todas as letras maiusculas
#o nome com todas as minusculas
#quantas letras ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome

nome = str(input('Digite um nome completo: ')).strip()
print(nome.upper())
print(nome.lower())
print(f'Ao todo, o nome completo tem {len(nome) - nome.count(' ')} palavras')
print(f'O primeiro nome tem {nome.find(' ')} palavras')
separa = nome.split()
print(f'Seu primeiro nome é {separa[0]} e seu nome tem {len(separa[0])} letras')


#23 faça um programa que leia um numero de 0 a 9999 e mostre na tela cada um dos digitos separados

#ex: digite o numero: 1834
#unidade: 4
#dezena: 3
#centena: 8
#milhar: 1

sequencia = str(input('Digite um valor entre 0 e 9999: ')).strip()
print('Analizando os valores temos:')
print(f'Unidade: {(sequencia[3:4])}')
print(f'Dezena: {(sequencia[2:3])}')
print(f'Centena: {(sequencia[1:2])}')
print(f'Milhar: {(sequencia[0:1])}')


#Correção:

num = int(input('Digite um numero: '))
u = num // 1 % 10
d = num // 10 % 10 
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: ', u)
print('Dezena: ', d)
print('Centena: ', c)
print('Milhar: ', m)


#24 Crie um programa que leia o nome de uma cidade e diga se ela comaça ou não com a palavra "SANTO"


cidade = str(input('Digite um nome de uma cidade: ')).strip().upper()
divide = cidade.split()
print(f'A cidade escolhida começa com {divide[0]}')
print(f'A cidade começa com SANTO verdadeiro ou falso: {'SANTO' in cidade}')


#25 Crie um programa que leia o nome de uma pessoa e diga se ela tem "silva" no nome (pode ser silva em qualquer lugar do nome)


nome = str(input('Digite um nome completo: ')).strip().upper()
print(f'Seu nome possui Silva, verdadeiro ou falso? {'SILVA' in nome}')



#26 faça um programa que leia uma frase pelo teclado e mostre:

#quantas vezes aparece a letra "A"
#em que posição ela aparece a primeira vez
#em que posição ela aparece a ultima vez

letras = str(input('Difite uma frase: ')).strip().upper()
print(f'A letra a aparece na frase {letras.count('A')} vezes. \nA letra a aparece a primeira vez na sequencia: {letras.find('A')}\nA ultima posiçao da letra a é: {letras.rfind('A')}')


#27 Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente. 

nome = str(input('Digite um nome completo: ')).strip()
print(f'Seu nome completo é: {nome}')
divisão = nome.split()
print(f'Seu primeiro nome é: {divisão[0]}')
print(f'Seu ultimo nome é {divisão[len(divisão) - 1]} ')


