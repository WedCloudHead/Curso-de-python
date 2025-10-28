#faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessario para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²

#como eu fiz:

altura = int(input('digite o valor de uma altura: '))
largura = int(input('digite o valor de uma largura de uma parede: '))
lata = int(2 ** 2)
parede = int(altura * largura * lata)
print(parede)


#como o professor demonstrou na correção:

larg = float(input('largura da parede: '))
alt = float(input('altura da parede: '))
área = larg * alt
print('sua parede tem a dimensão de {}x{} e sua área é de {}m². '.format(larg, alt, área))
tinta = área / 2
print('para pintar essa parede, voce precisara de {}L de tinta. '.format(tinta))