#Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.



#Primeira tentativa:

palavras = ('cavalo', 'forza', 'zangado', 'aviao', 'templo', 'trem', 'asfalto', 'festival', 'cultura')

vogais = palavras.split()

resultado = []

for p in palavras:
    if p in ['a', 'e', 'i', 'o', 'u']:
        resultado.append(p)
    
resultado_final = ' '.join(resultado)

print(f'Dentro da lista de palavras existem as seguintes vogais: {resultado_final}')



#Segunda tentativa:

palavras = ('cavalo', 'forza', 'zangado', 'aviao', 'templo', 'trem', 'asfalto', 'festival', 'cultura')


vogal = []

for v in palavras:
    if v in ['a', 'e', 'i', 'o', 'u']:
        vogal.append(v)


print(vogal)


#Terceira tentativa:

palavras = ('carneiro', 'asfalto', 'camelo', 'jacare', 'forza', 'japao', 'zangado', 'python')

vogais = []
itens = []
coleçao = []

for item in palavras:
    itens.append(item)
    for p in item:
        if p in ['a', 'e', 'i', 'o', 'u']:
            vogais.append(p)


print(itens[0] , vogais[0:4])

print(itens + vogais)

print(coleçao)



print(f'As vogais dentro da palavras carneiro e asfalto são: {vogais}')



#Quarta tentativa:


palavras = ('carneiro', 'asfalto', 'camelo', 'jacare', 'forza', 'japao', 'zangado', 'python')

vogais = []
itens = []
coleçao = []

for item in palavras:
    itens.append(item)
    for p in item:
        if p in ['a', 'e', 'i', 'o', 'u']:
            vogais.append(p)



while True:
    coleçao.append(itens + vogais)
    break

print(coleçao)




#Quinta tentativa:


palavras = ('carneiro', 'asfalto', 'camelo', 'jacare', 'forza', 'japao', 'zangado', 'python')

for p in palavras:
    print('--'*10)
    print(p)
    for v in p:
        if v in ('a', 'e', 'i', 'o', 'u'):
            print(v)
        

#Ainda não ta 100% mas só aqui eu consegui chegar a um resultado consideravelmente bom!



#Como professor demonstrou:


palavras = ('aprender', 'programar', 'linguagem', 'python',
            'logica', 'codigo', 'teclas', 'binario', 'programa',
            'curso', 'praticar', 'futuro', 'estrategista')


for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')




#CORREÇÃO PÓS EXPLICAÇÃO DO PROFESSOR:


palavras = ('carneiro', 'asfalto', 'camelo', 'jacare', 'forza', 'japao', 'zangado', 'python')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for v in p:
        if v.lower() in ('a', 'e', 'i', 'o', 'u'):
            print(v, end=' ')
        