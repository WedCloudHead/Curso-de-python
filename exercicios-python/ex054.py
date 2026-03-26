#Crie um programa que leia o ano de nascimento de sete pessoas. No final,
#mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores. (considere maior idade com 21 anos)


#Como eu fiz 

from datetime import date
for id in range(1, 8):
    usuarios = int(input('Digite seu ano de nascimento: '))
    atual = date.today().year
    idade = atual - usuarios
    if idade < 21:
        print(f'Você tem {idade} anos e ainda não atingiu a maioridade')
    elif idade >= 21:
        print(f'Você tem {idade} anos e já atingiu a maioridade')
    else:
        print('Comando incorreto, por favor tente de novo!')
print('Fim do programa!')


#Segunda resolução:

from datetime import date
hoje = date.today().year
for c in range(1, 8, 1):
    digite = int(input('Digite seu ano de nascimento: '))
    if not digite:
        print('Você não digitou valor algum!')
    else:
        try:
            if hoje - digite < 21:
                print(f'Você ainda não atingiu a maioridade! faltam {hoje - digite} anos!')
            else:
                print(f'Você já atingiu a maioridade, você tem {hoje - digite} anos!')
        except ValueError:
            print('Digite um valor numerico!')
print('Fim do contador!')


#Terceira resolução:

from datetime import date
try:
    usuario = int(input('Digite seu ano de nascimento: '))
except ValueError:
    print('Digite apenas números!')
else:
    maior_idade = 0
    menor_idade = 0
    for c in range(1,8):
        ano = date.today().year
        atual = ano - usuario
        usuario = int(input('Digite seu ano de nascimento: '))
        if atual < 21:
            usuario += menor_idade
        else:
            usuario += maior_idade
    print(f'Nessa contagem o total de pessoas de maioridade são: {atual}') #maior_idade
    print(f'Nessa contagem o total de pessoas de menoridade são: {atual}') #menor_idade
print('Fim do programa!')



#Quarta resolução:


from datetime import date 
maiores = 0
menores = 0

ano = date.today().year
for c in range(1,8):
    try:
        usuario = int(input(f'Digite seu ano de nascimento {c}: '))
        idade = ano - usuario

        if usuario > ano:
            print('Não é possivel você ter nascido no futuro nesse momento :()')
        elif usuario <= 1900:
            print('Se você tiver nascido antes ou em 1900 você teria hoje 126 anos ou mais, as chances de você estar vivo hoje são quase impossiveis!')
        else:
            idade = ano - usuario

            if idade >= 21:
                maiores += 1
            else:
                menores += 1 
    except ValueError:
        print('Digite apenas valores numericos!')
print(f'O total de pessoas maiores de idade são: {maiores}')
print(f'O total de pessoas menores de idade são: {menores}')


#Resolução do professor:


from datetime import date
atual = date.today().year 
totmaior = 0
totmenor = 0
for pess in range(1,8):
    nasc = int(input(f'Em que ano a {pess}ª pessoa nasceu? '))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print(f'Ao todo tivemos {totmaior} pessoas maiores de idade')
print(f'Ao todo tivemos {totmenor} pessoas menores de idade')



#Sobre a primeira resolução:
#Não resolve o problema sugerido, o que esse meu primeiro programa faz é ler individualmente
#cada data e dizer se já possui mais de 21 anos ou não.

#Sobre a segunda resolução:
#Também não resolve o problema pois faz praticamente a mesma coisa que a primeira resolução.

#Sobre a terceira resolução:
#Aqui já é possivel notar o início de uma lógica que já leva a um fim diferente; Meu programa
#lê em sequência as datas pedidas nos inputs e armazena as informações a cada ciclo do for
#porém eu errei ao finalizar, era só mudar a duas ultimas linhas dos prints finais 
#(linha 58 e 59) pois eu acabo pedindo pra printar as idades e não o total de pessoas.
#Detalhe EXTREMAMENTE IMPORTANTE: O tratamento de erro com try (linhas 43 a 45) estão quase
#que totalmente desfuncionais pois esse try alem de não impedir de travar o programa só 
#funcionam no primeiro input pois o try e o except estão fora do for.

#Sobre a quarta resolução:
#Agora sim nesse programa existe um tratamento de erro correto, da qual todas as opções de 
#input estão sujeitas a proteção do try do qual o programa só irá ler os inputs que cindizem
#com o que eu quero que é o que se pede no contexto do problema. 
#Os contadores estão armazenando as informações corretamente e os prints finais estão
#entregando corretamente a quantidade de pessoas selecionadas para o problema.


#Sobre a resolução do professor:
#Extremamente eficiente, poucas linhas e funcional! Detalhe interessante ele adiciona na 
#(linha 102) o comando {pess} que pega cada contador do for e trata nos inputs por
#demonstrando ordem; Detalhe simples mas super eficiente e sofisticado.