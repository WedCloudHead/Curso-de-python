nome = str(input('Qual o seu nome? ')).strip()
if nome == 'Gustavo':
    print('Que nome de professor em!')
else:
    print('Seu nome é de uma pessoa bem inteligente')
print(f'Bom dia, {nome}!')

#Essa é uma condição simples, apenas duas alternativas, apenas duas condições; se seu nome é estritamente Gustavo == que nome de professor.
#todo o resto == que nome de pessoa inteligente.


nota01 = float(input('Digite sua primeira nota: '))
nota02 = float(input('Digite sua segunda nota: '))
media = (nota01 + nota02)/2
print(f'sua media foi {media:.1f}')
if media >=6:
    print('Nada mal, parabens!')
else:
    print('Poderia ter sido melhor, estude mais!')





