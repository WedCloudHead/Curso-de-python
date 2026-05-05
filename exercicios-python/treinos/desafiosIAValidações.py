#Agora sim: seus 10 desafios de validação
#Vou montar progressivo — do mais simples ao mais “chatinho”.

#🔹 Desafio 1 — Nome obrigatório

#Peça o nome do usuário.

#Regras:

#não pode ser vazio
#deve ter pelo menos 3 caracteres



#🔹 Desafio 1 — Nome obrigatório

#Peça o nome do usuário.

#Regras:

#não pode ser vazio
#deve ter pelo menos 3 caracteres


#Forma de validação simples onde só aceita o primeiro nome com pelo menos 3 letras.


while True:
    nome = input('Digite seu nome: ').strip().title()
    if not nome:
        print('O campo precisa ser preenchido')
        continue
    
    if not nome.isalpha():
        print('Digite apenas letras')
        continue
    
    if len(nome) < 3:
        print('O nome precisa ter ao menos 3 caracteres')
    else:
        break

print(f'Nome {nome} cadastrado')
print('Fim da validação')



#Forma de validação mais complexa onde aceita nomes completos porem apenas letras.


while True:
    nome = input('Digite seu nome: ').strip().title()
    if not nome:
        print('O campo precisa ser preenchido')
        continue
    
    if len(nome) < 3:
        print('O nome precisa ter ao menos 3 caracteres')
        continue
    
    valido = True
    for letras in nome:
        if not letras.isalpha() and not letras.isspace():
            valido = False
            print('Digite apenas letras respeitando os espaços')
            break
    if not valido:
        continue
        
    break

print(f'Nome {nome} cadastrado')
print('Fim da validação')


#Forma de validação igualmente complexa, agora tornando nomes completos que não possuem maiusculas em seu meio.


while True:
    nome = input('Digite seu nome: ').strip().lower()
    if not nome:
        print('Preencha o campo corretamente')
        continue
    break

palavras = nome.split()

resultado = []

for p in palavras:
    if p in ['da', 'de', 'do', 'das', 'dos']:
        resultado.append(p)
    else:
        resultado.append(p.capitalize())

nome_resultado = ' '.join(resultado)

print(f'Nome {nome_resultado} cadastrado')






#🔹 Desafio 2 — Idade válida

#Peça a idade.

#Regras:

#só aceitar números
#não pode ser negativo
#não pode ser maior que 120


while True:
    try:
        idade = int(input('Digite sua idade: '))

        if idade <= 0:
            print('Não é aceito idades com 0 anos ou números negativos')
            continue
    
        if idade > 120:
            print('Não é aceito idades acima de 120 anos.')
            continue
        break
    except ValueError:
        print('Digite apenas números')

print(f'Fim da validação!')




#🔹 Desafio 3 — Letra específica

#Peça uma letra.

#Regras:

#aceitar apenas 1 caractere
#deve ser entre A e Z




#Primeira forma, já atende o pedido porem ainda aceita letras com acento:

while True:
    letra = input('Digite uma letra de A a Z: ').strip().upper()
    if not letra:
        print('O campo não pode estar vazio')
        continue
    
    if len(letra) != 1:
        print('Digite apenas 1 letra')
        continue
    
    if not letra.isalpha():
        print('Digite apenas letra')
        continue
          
    break   

print(f'Fim da validação! A letra escolhida foi {letra}')



#Segunda forma, mesma lógica porém agora ignorando acentos:


import string

letras_permitidas = string.ascii_uppercase

while True:
    letra = input('Digite uma letra de A a Z: ').strip().upper()
    if not letra:
        print('O campo não pode estar vazio')
        continue
    
    if len(letra) != 1:
        print('Digite apenas 1 letra')
        continue
    
    if not letra.isalpha():
        print('Digite apenas letra')
        continue
    
    if letra not in letras_permitidas:
        print('Digite apenas letra sem acentos de (A-Z)')
        continue
          
    break   

print(f'Fim da validação! A letra escolhida foi {letra}')





#🔹 Desafio 4 — Senha simples

#Peça uma senha.

#egras:

#mínimo 6 caracteres
#não pode ser vazia




while True:
    senha = input('Digite uma senha com mínimo de 6 caracteres: ').strip() #Usar .strip() para senhas depende do contexto, geralmente em sistemas reais não se usa.
    if not senha:
        print('O campo não pode estar vazio')
        continue
    
    if len(senha) < 6:
        print('A senha precisa ter no mínimo 6 caracteres')
        continue
    break

print('Fim da validação, Obrigado!')



#Desafio extra, agora a senha só pode ter 1 numero, 1 letra e 1 caractere especial.


while True:
    senha = input('Digite uma senha com mínimo de 6 caracteres: ').strip() #Usar .strip() para senhas depende do contexto, geralmente em sistemas reais não se usa.
    if not senha:
        print('O campo não pode estar vazio')
        continue
    
    if len(senha) < 6:
        print('A senha precisa ter no mínimo 6 caracteres')
        continue
    
    tem_numero = False
    tem_letra = False
    tem_especial = False
    for s in senha:
        if s.isdigit():
            tem_numero = True
        elif s.isalpha():
            tem_letra = True            
        elif not s.isspace():
            tem_especial = True
            
                
    if not tem_numero:
        print('É preciso ter pelo menos 1 número')
        continue


    if not tem_especial:
        print('É preciso ter pelo menos 1 caractere especial')
        continue
    

    if not tem_letra:    
        print('É preciso ter pelo menos 1 letra')
        continue

    break

print('Fim da validação, Obrigado!')


#OBS: Esse código não resolve diretamente o problema da caractere especial porem no (file colas) tem um exemplo de duas formas que torna possivel fazer:




#🔹 Desafio 5 — Número positivo obrigatório

#Peça um número inteiro.

#Regras:

#deve ser número
#maior que 0




while True:
    try:
        entrada = (input('Digite um número qualquer que seja maior que 0: '))
        if not entrada:
            print('O campo não pode estar vazio!')
            continue
        usuario = int(entrada)
        if usuario <= 0:
            print('O valor digitado precisa de maior que zero!')
            continue
    except ValueError:
        print('Digite apenas números')
        continue
    
    break
print('Fim do programa!')







#🔹 Desafio 6 — Escolha de menu

#Mostre:

#1 - Jogar
#2 - Sair

#Regras:

#aceitar só 1 ou 2
#tratar erro de entrada


#Primeira forma: (precisa corrigir)

usuario = None

while usuario != 2:
    try:
        usuario = int(input('Digite o número 1 para jogar e número 2 para sair: '))
    except ValueError:
        print('Digite apenas números')
        continue

    if usuario == 1:
        print('1 selecionado')

    if usuario == 2:
        break


print('Fim do programa')




#Segunda forma:

while True:
    try:
        entrada = input('Digite 1 para jogar e 2 para sair: ').strip()
        if not entrada:
            print('O campo não pode estar vazio') 
            continue
        usuario = int(entrada)
        if usuario not in (1, 2): #pode ser [1, 2] também, parenteses é mais leve
            print('Digite apenas 1 ou 2')
            continue
        if usuario == 1:
            print('1 selecionado')
        elif usuario == 2:
            break
        
    except ValueError:
        print('Digite apenas números')

print('Fim do programa')





#🔹 Desafio 7 — Par ou Ímpar (validação pura)

#Peça “P” ou “I”

#Regras:

#aceitar “par”, “p”, “impar”, “i”
#rejeitar vazio
#usar só a primeira letra

#(esse você praticamente já fez)



while True:
    usuario = input('Escolha P(par) ou I(impar): ').strip().upper()
    if not usuario:
        print('O campo não pode estar vazio')
        continue
    if not usuario.isalpha():   #Esse bloco nesse problema em especifico é reduntante, poderia deixar apenas os demais bolocos, daria o mesmo resultado, pois quando se filtra pela primeira linha como ('PI') automaticamente já filtra todo resto 
        print('Digite apenas letras')  
        continue
    
    primeira = usuario[0]
    if primeira not in 'PI':
        print('Ecolha entre P ou I')
        continue
    usuario = primeira
    break
print('Fim do programa')







#🔹 Desafio 8 — Número dentro de intervalo

#Peça um número entre 1 e 10.

#Regras:

#deve ser número
#deve estar dentro do intervalo


while True:
    try:
        num = int(input('Digite um número entre 1 e 10: '))
       
    except ValueError:
        print('Digite apenas números')
        continue
    
    if num < 1 or num > 10: #tambem pode ser escrito como:  if not 1 <= num <= 10:   É a mesma coisa.
        print('digite apenas valores entre 1 e 10')
        continue
    
    break

print('Fim do programa')


'''
Como deixar melhor o tratamento de vazio:

entrada = input(...).strip()

if not entrada:
    print('O campo não pode estar vazio')
    continue

num = int(entrada)
'''



#🔹 Desafio 9 — Confirmação de senha

#Peça uma senha e depois confirme.

#Regras:

#devem ser iguais
#não pode ser vazia




while True:
    senha = input('Digite uma senha: ')
    if not senha:
        print('O campo não pode estar vazio')
        continue
    while True:
        senha2 = input('Confirme a senha digitada: ')
        if not senha2:
            print('O campo não pode estar vazio')
            continue
        if senha2 != senha:
            print('As senhas digitadas não batem!')
            continue
        if senha2 == senha:
            print('Senha confirmada com sucesso!')

            break
    break
print('Senha confirmada! fim do programa.')

'''
Outra forma de fazer e mais simplificado:

while True:
    senha = input('Digite uma senha: ')
    if not senha:
        print('O campo não pode estar vazio')
        continue
    senha2 = input('Confirme a senha digitada: ')
    if not senha2:
        print('O campo não pode estar vazio')
        continue
    if senha2 != senha:
        print('As senhas digitadas não batem!')
        continue
    else:
        print('Senha confirmada com sucesso')

    break


'''




#🔹 Desafio 10 — Sistema completo (nível acima)

#Peça:

#nome
#idade
#escolha (P ou I)

#Regras:

#validar tudo corretamente
#só prosseguir quando tudo estiver válido


while True:
    nome = input('Digite seu nome: ').strip().lower()
    if not nome:
        print('Preencha o campo corretamente')
        continue
    
    while True:
        try:
            idade = int(input('Digite sua idade: '))
        except ValueError:
            print('Digite apenas números')
            continue
        if not 0 < idade < 120:
            print('Digite apenas idades reais')
            continue
        break
    
    while True:
        escolha = input('Escolha entre  P(par) ou I(impar): ').strip().upper()
        if not escolha:
            print('Preencha o campo corretamente')
            continue
        primeira = escolha[0]
        if primeira not in 'PI':
            print('Escolha entre P ou I')
            continue
        escolha = primeira

        break
    break


palavras = nome.split()

resultado = []

for p in palavras:
    if p in ['da', 'de', 'do', 'das', 'dos']:
        resultado.append(p)
    else:
        resultado.append(p.capitalize())

nome_resultado = ' '.join(resultado)


print(nome_resultado, idade, escolha)


print('Fim do programa')


#🚀 Como fazer esses desafios

#Regra geral:

#👉 Sempre usar esse padrão:


#while True:
    #entrada = input(...)

    #if inválido:
        #print(...)
        #continue

    #break




#🎯 Próximo passo

#Se quiser evoluir ainda mais, posso:

#corrigir suas soluções desses desafios
#ou te passar versões com nível “profissional iniciante”