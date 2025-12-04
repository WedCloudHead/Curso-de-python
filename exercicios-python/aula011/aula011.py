#Adicionando cores ao terminal e testando:

print('\033[4;33;40mHello friend\033[m')
print('\033[0;31;41m---\033[m' * 5)
print('\033[7;37;40mRoot\033[m')
print('\033[0;31;41m---\033[m' * 5)
print('\033[1;32;44mWhoami\033[m') 
print('\033[0;31;41m-=-\033[m' * 5)
print('\033[4;35;40musermod\033[m')
print('\033[0;31;41m-=-\033[m' * 5)

#praticando a inversão de cores:

print('\033[0;32;43mletra verde fundo amarelo\033[m')
print('\033[7;32;43mletra amarela fundo verde\033[m')
#na verdade ficou com a letra petra
print('\033[0;31;41m-=-\033[m' * 5)
print('\033[1;33;44mdeluser\033[m')
print('\033[7;33;44mdeluser\033[m')
print('\033[4;30;41mfundo vermelho letra branca\033[m')
print('\033[7;30;41mfundo branco letra vermelha\033[m')
print('\033[0;31;41m-=-\033[m' * 5)
#na verdade ficou com fundo preto
#aparentemente o ANSI tem dificuldade a inverter as
#cores das linhas com as cores do fundo!

#praticando cores nas variaveis:

num1 = 5
num2 = 6
num3 = 7

print(f'Os valores são \033[32m{num1}\033[m, \033[31m{num2}\033[m e \033[34m{num3}\033[m')

# agora com cor de fundo nas letras


num1 = 5
num2 = 6
num3 = 7

print(f'Os valores são \033[32;45m{num1}\033[m, \033[31;45m{num2}\033[m e \033[34;45m{num3}\033[m')

print('\033[0;31;41m-=-\033[m' * 5)


#Extra é muito bom o sistema de cores para destacar alguma informação em especifico no codigo ou por exemplo quando se quer demonstrar que tal grafico ou valor esta em queda ou negativo, dai modificaria ele para cor vermelha, o contrario seria o verde e assim por diante, não é um detalhe essencial para programar em si mas é de fato um conhecimento adicional 