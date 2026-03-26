#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No
#final, mostre os 10 primeiros termos dessa progressão.


#Cono eu fiz:


usuario1 = int(input('Digite o primeiro termo da PA: '))
usuario2 = int(input('Digite a razão da PA: '))
usuario3 = int(input('Digite o limite da PA: '))
for c in range(usuario1, usuario3, usuario2):
    print(c)
print(f'O primeiro termo dessa PA é: {usuario1}')
print(f'A razão dessa PA é: {usuario2}')
print('Os 10 primeiros termos dessa PA são: ')
for c in range(usuario1, 10, usuario2):
    print(c)
print('fim')



#Após voltar treinando e praticando esse foi meu segundo modo de refazer o desafio (03/03/2026):

conta = int(input('Digite o termo da PA:'))
conta2 = int(input('Digite a razão da PA: '))

for c in range(0, conta, conta2):
    print(c)
print('--' * 20)
print(f'Os 10 primeiros termos dessa PA são: ')
for c in range(0, conta // 2, conta2):
    print(c)

print('Fim do programa!')


#Ao fim da resolução do professor virar a explicação desse meu novo método que usei para refazer o exercicio.


#Como o professor demonstrou:


primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
décimo = primeiro + (10 - 1) * razão
for c in range(primeiro, décimo + razão, razão):
    print(f'{c}', end=' > ')
print('Acabou!')



#Sobre minha primeira resolução:
# Achei interessante que eu consegui fazer com que o meu programa definice
#um inicio e um limite da PA, porém, eu não soube como pegar individualmente somente os 10 primeiros termos da PA.

#Sobre a segunda resolução:
#Já é possivel notar um avanço no raciocinio lógico usado nesse programa pois eu 
#consegui não só resolver o problema como entregar separadamente os 10 
#primeiros termos da PA como é pedido no desafio, o problema é que ainda sim
#o programa foi resolvido quase que como quem sabe "daria pra ter feito melhor"
#O programa cumpre seu papel mas poderia ter tido uma estrutura indentada mais sofisticada.

#Sobre a resolução do professor:
#É onde cobre o buraco da minha segunda resolução, o programa do professor 
#também resolve o problema e mantem uma estrutura totalmente bem encaixada.
#armonica com o que se diz respeito ao aninhamento da estrutura da programação.


