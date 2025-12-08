#Exemplos de condições aninhadas:

#lembrando que esses codigos não estavam na aula exatamente como esta aqui, eu mesmo que fiz por conta propria:

carro = str(input('Diga um nome de um carro: '))
if carro == 'Mitsubishi':
    print('Esse é um bom carro japonês!')

elif carro == 'Lamborghini' or carro == 'Porshe' or carro == 'BMW':
    print('São monstros de carros')

elif carro in 'Ferrari Volkswagen Mercedes':
    print('É de uma procêdencia duvidosa!')

elif carro in 'Lambo Lamborgini lambo lamborgini lamborgine Lamborgine Lambo':
    carro = str(input('Vocẽ quis dizer Lamborghini? '))
if carro == 'yes' or 'sim':
    print('o carro Lamborghini é foda!')

elif carro in 'Wolksvagem Volksvaguem Volqsvagem wolksvagem volksvaguem volqsvagem volksvagen Volksvagen volksvagem Volksvagem':
    print('Você quis dizer Volkswagen?')

elif carro in 'Mitsubichi mitisubichi mitisubiche Mitisubichi Mitisubiche':
    print('você quis dizer Mitsubishi?')

else: 
    print('Você não perde nada em não falar uma marca de carro!')
print('Tenha uma ótima vida!!')


#Como professor demosntrou na aula:

nome = str(input('Qual é seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Pedro':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia, {nome}!')