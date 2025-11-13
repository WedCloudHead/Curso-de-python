#crie um programa que leia o nome de uma cidade e diga se ela comaça ou não com a palavra "SANTO"

#Como eu fiz:

Cidade = 'São João Nepomuceno'
Cidade2 = 'Santo Miguel das Flores'

print('Santo' in Cidade)
print('Santo' in Cidade2)


#Como professor demonstrou:

cidade = str(input('Digite o nome de uma cidade da forma que você quiser: ')).strip()

print(cidade[:5].upper() == 'SANTO')

separa = cidade.split()

#Uma forma de aprimorar o codigo caso a palavra santo não apareça somente no inicio do nome.
#(lembrando que foi feito por mim entao pode haver erros    )

print(separa[0], separa[1].upper() == 'SANTO')

#Extra: 

#Uma boa pratica é tentar afunilar o maximo o possivel as variaveis de erro, ou seja nesse problema o usuario poderia escrever santo de diversas formas, Santo, SANto, sANto, sanTO, SaNtO, etc, o que o programa faz é pegar todas as variaveis da palavra santo e jogar toda ela para maiusculo, ou seja, idependente da forma que seja escrito santo, sera tudo jogado ao maiusculo e depois sera analizado se na palavra existe a sequencia S_A_N_T_O idependente se estao em maiusculos ou minusculos na hora que o usuario responder.