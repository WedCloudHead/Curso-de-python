#faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente

#ex: Ana Maria de Souza
#primeiro: Ana
#ultimo: Souza


# como eu fiz:

nome = 'Walter Julio Roberto de Souza'

print(nome[0:7])

print(nome.find('Souza'))

print(nome[24:29])


#tentando melhorar o codigo:

nome = str(input('Digite um nome completo qualquer: ')).strip()

print(nome)

separa = nome.split()

print(separa[0])

print()

#Novamente o ultimo problema não consegui resolver, ficando novamente 2/3 do problema resolvido apenas


#como professor demonstrou:

n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('seu primeiro nome é {} '.format(nome[0]))
print('seu ultimo nome é {} '.format(nome[len(nome)-1]))


#extra:

#sempre importante aprender com os erros, nesse caso eu não entendi inteiramente a logica por tras dos usos dos metodos para resolver esses exercicios de forma segura, preciso treinar mais!


#na linha 39 o que foi usado é metodo len; basicamente ele pegou a declaração nome (splitado ja) e atribiu o metodo len ficando nome[len], entao dentro de len é preciso dizer qual declaraçao ele quer que o len traga de forma integral, ficando assim nome[len(nome)] dessa forma o len vai trazer o nome completo idependente de qual tamanho for e com adicional de que o nome ja vai estar separado por camadas graças ao split (nome = n.split()) e no final para matar 100% o problema ele adicionou o -1 ou seja o metodo len vai pegar o nome completo dividido por grupos porem com -1 ele vai voltar um grupo que seria o ultimo ficando nome[len(nome)-1] 
#o que ele faz na pratica:

#Roberto Ficher Marinho Souza = Roberto(0) Ficher(1) Marinho(2) Souza(3) fim(4) o len vai pegar e devolver integralmente 1,2,3,4 e finalizar ou seja ; o -1 vai fazer ele voltar um grupo (4 = 3) do finalizar ele vai para Souza fazendo com que assim mostre sempre o ultimo nome idependente do tamanho.



