#Crie um programa que leia o nome completo de uma pessoa e mostre:

# o nome com todas as letras maiusculas
#o nome com todas as minusculas
#quantas letras ao todo (sem considerar espaços)
#quantas letras tem o primeiro nome

#como eu fiz:

nome = 'Wederson da Silva Torres'

print('Seu nome em maiusculas é: ',nome.upper())

print('Seu nome em minusculas é: ',nome.lower())

print('Ao todo seu nome tem: ',nome.strip(), 'letras')

print('Seu primeiro nome tem: ',nome[0:9], 'letras')

#como professor demonstrou:

nome = str(input('Digite seu nome completo: ')).strip()

print('Analizando seu nome...')

print('Seu nome em maiusculas é: {}'.format(nome.upper()))

print('Seu nome em minusculas é: {}'.format(nome.lower()))

print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' '))) 

print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))

separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

print('Seu segundo nome é {} e ele tem {} letras'.format(separa[1], len(separa[1])))

#treinando mais um pouco:

nome = str(input('Digite um Nome completo: ')).strip()

grupo = nome.split()

print('Seu nome em maiusculas é {},\n seu nome em minusculas é {},\n ao todo seu nome tem {} letras,\n seu primeiro nome tem {} letras '.format(nome.upper(), nome.lower(),len(nome) - nome.count(' '), nome.find(' ')))

print(f'Seu nome em maiusculas é {nome.upper()}')

print(f'Seu nome em munusculas é {nome.lower()}')

print(f'seu primeiro nome é {nome.find(' ')}')

print(f'seu nome ao todo tem {len(nome) - nome.count(' ')}')

print(f'seu primeiro nome é {grupo[0] }')



#Inmportante:

#Linha 30)
#importantissimo gravar essa forma de conjulgar os metodos
#como nesse exemplo em que eu quero que o python leia somente a quantidade de letras no nome
#ignorando os espaços, entao usa-se os metodos dessa forma:
#print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
#lembrando que len(nome) é usado para analizar os caracteres de forma integral contando os espaços
# e ao adicionar - nome.count(' ') ou seja - = menos, nome.count() = metodo de contagem, (' ') = aspas com espaço dentro
#significa: conte as caracteres ignorando todos os espaços e considerando apenas as letras. 


#Linha 32)
#o metodo nome.find(' ') é usado para que o ele encontre quantos caracteres ha ate o primeiro espaço, consequentimente numerando quantas letras tem o primeiro nome da pessoa


#Linha 34/37) 
#a divisao por classes utilizando o split é essencial para achar um grupo de caracteres em qualquer local de um conjunto de caracteres pois ao declarar por exemplo:

#nome = str(input('Digite seu nome completo: '))
#e esse nome tenha as seguintes caracteres: Luisa Souza Rocha de Almeida
#como faria para que fosse printado somente o Souza ou Rocha?
# ai entra o .split()
#basicamente voce cria uma declaração pra ele como:
#separa = nome.split() ou grupo = nome.split() tanto faz
#o essencial que ao utilizar ele pedindo pra que ele te de as caracteres que estao presentes em seus grupos ele vai encontrar com exatidao, entao por exemplo, em Luisa Souza Rocha de Almeida existem 5 grupos de caracteres: Luisa 1 Souza 2 Rocha 3 de 4 Almeida 5; ao pedir que o split te devolva o resultado do grupo 4, 3 tanto faz, ele vai te entregar com exatidao a quantidade desse grupo
#print(separa[0], len(separa[0])) 
#ou 
#print(grupo[3], len(grupo[3])) 
#aqui basicamente eu to pedindo aos metodos [] e len() que me entreguem as informaçoes dos respectivos grupos que estao dentro de [] e (). 