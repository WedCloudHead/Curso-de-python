
#BLOCO NÍVEL 2 — Python Lógica + Estruturas Esses exercícios vão subir um degrau. 

#🧩 EXERCÍCIO 1 — Ranking de alunos Leia o nome e a nota de 5 alunos. Mostre: nome do aluno com maior nota nome do aluno com menor nota média da turma lista dos alunos acima da média 💡 desafio extra: tratar empate no maior. 



maior_nota = 0
menor_nota = 0
nome_maior_nota = 0
nome_menor_nota = 0
soma_notas = 0
listas_notas = []
listas_nomes = []
listas_maiores_notas = []
nomes_maiores_notas = []
acima_media = []


for contador in range(5):
    while True:
        try:
            nome = str(input('Digite o nome: ')).strip().capitalize()
            nota = float(input('Digite uma nota: '))
            listas_nomes.append(nome)
            listas_notas.append(nota)
            break
        except ValueError:
            print('Digite apenas valores númericos')

    soma_notas += nota

    if contador == 0:
        maior_nota = nota
        menor_nota = nota
        nome_maior_nota = nome
        nome_menor_nota = nome
        nomes_maiores_notas.append(nome_maior_nota)
        listas_maiores_notas.append(maior_nota)
    else:
        if nota > maior_nota:
            maior_nota = nota
            nome_maior_nota = nome
            listas_maiores_notas = [maior_nota]
            nomes_maiores_notas = [nome_maior_nota]
        elif nota == maior_nota:
            listas_maiores_notas.append(nota)
            nomes_maiores_notas.append(nome)
        else:
            if nota < menor_nota:
                menor_nota = nota
                nome_menor_nota = nome

media = soma_notas / len(listas_notas)

for c in range(len(listas_notas)):
    if listas_notas[c] > media:
        acima_media.append(listas_nomes[c])

print(f'A média é: {media}')
print(f'Os nomes com as maiores notas são: {nomes_maiores_notas}, A lista com as maiores notas: {listas_maiores_notas}')
print(f'O nome do aluno com menor nota : {nome_menor_nota}')
print(f'Lista com as notas acima da média: {acima_media}')






#🧩 EXERCÍCIO 2 — Sistema de estoque simples Leia 5 produtos e suas quantidades. Mostre: produto com maior quantidade produto com menor quantidade média de estoque produtos abaixo da média 👉 aqui você começa a pensar em sistema real. 





produto_com_maior_quantidade_nome = []
produto_com_menor_quantidade_nome = []
produto_com_maior_quantidade = []
produto_com_menor_quantidade = []
maior_quantidade_produtos = 0
menor_quantidade_produtos = 0
produtos_abaixo_media = []
lista_nomes_dos_produtos = []
lista_quantidade_dos_produtos = []
soma_produtos = 0

for c in range(5):
    while True:
        try:
            nomes_Produtos = str(input('Digite o nome do produto: ')).strip().capitalize()
            quantidade_Produtos = int(input('Digite a quantidade desse produto: '))
            lista_nomes_dos_produtos.append(nomes_Produtos)
            lista_quantidade_dos_produtos.append(quantidade_Produtos)
            break
        except ValueError:
            print('Digite conforme o sugerido')

    soma_produtos += quantidade_Produtos


    if c == 0:
        maior_quantidade_produtos = quantidade_Produtos
        menor_quantidade_produtos = quantidade_Produtos
        produto_com_maior_quantidade.append(maior_quantidade_produtos)
        produto_com_menor_quantidade.append(menor_quantidade_produtos)
        produto_com_maior_quantidade_nome.append(nomes_Produtos)
        produto_com_menor_quantidade_nome.append(nomes_Produtos)
                
    else:
        if quantidade_Produtos > maior_quantidade_produtos:
            maior_quantidade_produtos = quantidade_Produtos
            produto_com_maior_quantidade = [maior_quantidade_produtos]
            produto_com_maior_quantidade_nome = [nomes_Produtos]
        elif quantidade_Produtos < menor_quantidade_produtos:
            menor_quantidade_produtos = quantidade_Produtos
            produto_com_menor_quantidade = [menor_quantidade_produtos]
            produto_com_menor_quantidade_nome = [nomes_Produtos]        
        elif quantidade_Produtos == maior_quantidade_produtos:
            produto_com_maior_quantidade.append(maior_quantidade_produtos)
            produto_com_maior_quantidade_nome.append(nomes_Produtos)
        elif quantidade_Produtos == menor_quantidade_produtos:
            produto_com_menor_quantidade.append(menor_quantidade_produtos)
            produto_com_menor_quantidade_nome.append(nomes_Produtos)

media = soma_produtos / len(lista_quantidade_dos_produtos)

for estoque in range(len(lista_quantidade_dos_produtos)):
    if lista_quantidade_dos_produtos[estoque] < media:
        produtos_abaixo_media.append(lista_nomes_dos_produtos[estoque])




print(f'Os produtos com maiores quantidades são: {produto_com_maior_quantidade_nome}, e suas quantidades são: {produto_com_maior_quantidade}')
print(f'Os produtos com menores quantidades são: {produto_com_menor_quantidade_nome}, e suas quantidades são: {produto_com_menor_quantidade}')
print(f'A media de produtos no estoque é {media}')
print(f'O estoque de produtos abaixo da média são: {produtos_abaixo_media}')






#🧩 EXERCÍCIO 3 — Lista separada por categoria Leia 10 números. Separe em 3 listas: pares ímpares múltiplos de 5 Mostre todas. ⚠️ Um número pode aparecer em mais de uma lista. 


lista_pares = []
lista_impares = []
lista_multiplos = []


for _ in range(10):
    while True:
        try:
            num = int(input('Digite um número qualquer: '))
            break
        except ValueError:
            print('Digite apenas valores númericos')


    if num % 2 == 0:
        lista_pares.append(num)
    else:
        lista_impares.append(num)
    if num % 5 == 0:
        lista_multiplos.append(num)
    
if not lista_pares:
        print('Total de zero números pares digitados')
if not lista_impares:
    print('Total de zero números impares digitados')
if not lista_multiplos:
        print('Não foram digitados nenhum valor multiplo de 5')



print(f'Todos os números pares digitados: {lista_pares}')
print(f'Todos os números impares digitados: {lista_impares}')
print(f'Todos os valores que são multiplos de 5 digitados: {lista_multiplos}')





#🧩 EXERCÍCIO 4 — Mini boletim Leia nome e 3 notas de 4 alunos. Mostre: média individual de cada aluno aluno com maior média aluno reprovado (< 6) 🔥 aqui entra raciocínio mais composto. 


#IMPORTANTE: ESSE EXERCÍCIO TÁ INCOMPLETO E ERRADO! 

nome_maior_nota = 0
maior_nota = 0
nome_menor_nota = 0
menor_nota = 0
soma_notas = 0
guarda_notas = []
guarda_nomes = []


for c in range(4):
    while True:
        try:
            nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
            nota = float(input('Digite a nota: '))
            if nota < 0 or nota > 10:
                print('Digite apenas notas maiores que 0 ou menores que 10')
            else:
                break
        except ValueError:
            print('Digite como sugerido')
    
    soma_notas += nota
    
if c == 0:
    nome_maior_nota = nome
    maior_nota = nota
    nome_menor_nota = nome
    menor_nota = nota
    guarda_notas.append(nota)
    guarda_nomes.append(nome)
    
else: 
    if nota > maior_nota:
        maior_nota = nota
        nome_maior_nota = nome
    elif nota < menor_nota:
        menor_nota = nota
        nome_menor_nota = nome
    elif maior_nota == nota:
        maior_nota = nota
        nome_maior_nota = nome
        guarda_notas = [nota]
        guarda_nomes = [nome]

media = soma_notas / 4



print(f'A média das notas é: {media}')
print(f'O aluno com a menor média é {nome_menor_nota} com {menor_nota}')
print(f'O aluno com a maior média é {nome_maior_nota} com {guarda_notas}')


if nota < 6:
    guarda_nomes.append(nome)
    guarda_notas.append(nota)
    print(f'Alunos reprovados aparecerão aqui: {guarda_nomes} com notas menores que 6.0, nota: {guarda_notas}')
    
print('fim')



#🧩 EXERCÍCIO 5 — Menu interativo Crie um programa com menu: 1 - Adicionar número 2 - Mostrar lista 3 - Mostrar maior 4 - Mostrar média 5 - Sair 👉 usa while True. Esse exercício é MUITO importante. 

#Primeira tentativa:


media_fim = 0
vezes = 0
somanum = 0
usuario = 0
listas = []

while usuario != 5:
    print('''
    1 - Adicionar número 
    2 - Mostrar lista 
    3 - Mostrar maior 
    4 - Mostrar média 
    5 - Sair 
        ''')
    while True:    
        try:
            usuario = int(input('Sua escolha: '))
            break
        except ValueError:
            print('Escolha somente as opções sugeridas')

    if usuario not in (1, 2, 3, 4, 5):
        print('Escolha somente entre os números sugeridos')


    if usuario == 1:
        print('Qual número você deseja adicionar? ')
        usuario0 = int(input('Digite um número: '))
        listas.append(usuario0)
        somanum += usuario0
        vezes += 1
        media_fim = somanum / vezes
        
    elif usuario == 2:
        print(f'Os números na lista até o momento: {listas}')

    elif usuario == 3:
        if listas:
            print(f'dentro da lista {listas}, o maior número é: ', max(listas))
        else:
            print(f'Sem números dentro da lista: {listas}')
        
    elif usuario == 4:
        if listas:
            media = somanum / vezes
            print(f'Numeros na lista: {listas}, A media entre eles: {media:.2f}')
        else:
            print(f'Não há números dentro da lista: {listas}')
        
    else: 
        usuario == 5
        print('Obrigado!')


media_final = media_fim

if not media_final:
    print('Não teve média pois a lista está vazia')
else:
    print(f'Sua média: {media_final:.2f}')

if not listas:
    print('Não teve número dentro da lista')
else:
    print(f'O maior número dentro da lista: ', max(listas))

if not listas:
    print('Não tiveram números cadastrados na lista')
else:
    print(f'Todos os números na lista: {listas}')


print('Fim do programa')


    
#Finalmente foi!!!!!!!!!!!!!
#Tô morrendo de fome, valeu <3



#🧩 EXERCÍCIO 6 — Frequência de números Leia 10 números. Mostre: qual número apareceu mais vezes quantas vezes apareceu lista sem repetidos 💡 começa a preparar terreno para dicionário. 







lista_numeros = []

#Entrada de dados:
for _ in range(10):
    while True:
        try:
            num = int(input('Digite um número: '))
            lista_numeros.append(num)
            break
        except ValueError:
            print('Digite apenas números')

#Variáveis de controle
maior_quantidade = 0
numero_mais_frequente = None
Lista_valores_unicos = []

#Processamento
for n in lista_numeros:

    #Criando lista repetidos
    if n not in Lista_valores_unicos:
        Lista_valores_unicos.append(n)

    #Contando quantas vezes o número aparece
    quantidade = lista_numeros.count(n)

    #Verificando se é o que mais aparece
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        numero_mais_frequente = n

#Saída
print(f'Lista original: {lista_numeros}')
print(f'Número mais frequente: {numero_mais_frequente}')
print(f'Quantidade de vezes: {maior_quantidade}')
print(f'Lista sem repetidos: {Lista_valores_unicos}')




#NOVO EXERCÍCIO — Ranking de números Leia 6 números e mostre: Qual número aparece mais vezes, Quantas vezes ele aparece, Lista sem repetidos. Quantos números aparecem apenas 1 vez


#É importante lembrar que nesse tipo de problema eu tô trabalhando com pelo menos 3 coisas diferentes: Contagem, Comparação e Evitar diplicados.


#Lista que é criada pra guardar os números do input
lista_numeros = []

#Guadando input com tratamento de erro, nada de novo até aqui
for _ in range(6):
    while True:
        try:
            num = int(input('Digite um número: '))
            lista_numeros.append(num)
            break
        except ValueError:
            print('Digite apenas números')


#Criando as variáveis e listas que serão usadas no for que vai percorrer os números do input um por vez

#Começa com vazio porque ainda não existe um número que mais repete
num_que_mais_repete = None 
#maior quantidade começa com 0 porque ainda não tem um número com maior quantidade
maior_quantidade = 0
#lista pra adicionar o valor que será único depois (se tiver)
lista_sem_repetidos = []
#lista pra adicionar o número que mais aparecer depois
numero_aparece_uma_vez = []

#Agora sim, o for que percorrera cada número do input
for n in lista_numeros:
    

    #Primeira coisa levar os números para uma variável para poder comparar depois e atualizar (caso precise)
    quantidade = lista_numeros.count(n)


    #Criando a comparação com atualização 
    #quantidade sempre será maior que maior quantidade porque maior quantidade começa com zero
    if quantidade > maior_quantidade:
        maior_quantidade = quantidade
        #Basicamente o essa lista so funciona por causa dessa comparação que é feita antes, a cada volta que o for dar, ele analiza se o número é o mais repetido dentro do quantidade = lista_numeros(n) se for mais repetido salva no num_que _mais_repete se não ele recebe false e não guarda 
        num_que_mais_repete = n

    #Essa condição pergunta se na primeira volta do for o número está dentro da lista_sem_repetidos, obviamente o primeiro não estará porque ela ta vazia, então ela guarda o primeiro número, na segunda volta a condição pergunta, esse segundo número já está ai dentro? se não, guarda, se sim, pula esse, e assim vai indo até percorrer todos os números, se não tiver um igual ai dentro, guarda, se já tiver, não guarda
    if n not in lista_sem_repetidos:
        lista_sem_repetidos.append(n)

    #Essa condição pergunta se tem algum valor dentro do quantidade que recebeu o quantidade = lista_numeros.count(n) só tem 1 unico dele, se tiver adiciona na lista numero_aparece_uma_vez.append(n)
    if quantidade == 1:
        numero_aparece_uma_vez.append(n)

print(f'Número que mais aparece {num_que_mais_repete}')
print(f'Quantidade de vezes que aparece {maior_quantidade}')
print(f'A lista sem repetidos {lista_sem_repetidos}')
print(f'O número que aparece uma única vez (caso tenha) {numero_aparece_uma_vez}')





#🧩 EXERCÍCIO 7 — Dicionário de alunos ⭐ Crie um dicionário com: { nome: nota } para 5 alunos. Mostre: maior nota menor nota média nomes acima da média 👉 aqui você sobe MUITO de nível. 


maior_nomes_nota = []
menor_nome_nota = ''
maior_nota = 0
menor_nota = 0
soma_notas = 0
lista_nomes = []
lista_notas = []
acima_media_nomes = []

for c in range(5):
    while True:
        try:
            nome = input('Digite um nome: ').strip().capitalize()
            if not nome:
                print('O campo nome não pode estar vazio.')
                continue
            if not nome.isalpha():
                print('Digite apenas letras')
                continue
            lista_nomes.append(nome)
            break
        except IndexError:
            print('Digite conforme o sugerido')

    while True:
        try:    
            entrada = input('Digite uma nota: ')
            if not entrada:
                print('O campo nota não pode estar vazio.')
                continue
            nota = float(entrada)
            if nota < 0 or nota > 10:
                print('A nota não pode ser menor que 0 ou maior que 10')
                continue
            lista_notas.append(nota)
            soma_notas += nota
            break
        except ValueError:
            print('Digite apenas números')

    if c == 0:
        maior_nota = nota
        maior_nomes_nota = [nome]
        menor_nome_nota = nome
        menor_nota = nota
    else:
        if nota > maior_nota:
            maior_nota = nota
            maior_nomes_nota = [nome]
        elif nota == maior_nota:
            maior_nomes_nota.append(nome)
          
        if nota < menor_nota:
            menor_nota = nota
            menor_nome_nota = nome


media = soma_notas / 5


for i in range(len(lista_notas)):
    if lista_notas[i] > media:
        acima_media_nomes.append(lista_nomes[i])


        
    


print(f'A média é {media:.2f}')
print(f'A maior nota é {maior_nota} dos(as) alunos(as) {maior_nomes_nota}')
print(f'A menor nota é {menor_nota} do aluno(a) {menor_nome_nota}')
print(f'As notas acima da média são: {acima_media_nomes}')
print('Fim')





#🧩 EXERCÍCIO 8 — Cadastro de pessoas Leia nome e idade de 5 pessoas. Mostre: mais velha mais nova média de idade quantos são maiores de idade 👉 ótimo treino para dados mistos. 



#🧩 EXERCÍCIO 9 — Função de estatísticas ⭐ Crie uma função: def analisar(lista): que receba uma lista e retorne: média maior menor quantidade acima da média 🔥 aqui começa modularização. 



#🧩 EXERCÍCIO 10 — Mini sistema final 💥 Monte um programa que permita cadastrar alunos com notas até o usuário sair. No final mostre: ranking maior nota média geral aprovados reprovados quantidade cadastrada 👉 esse fecha o bloco nível 2.