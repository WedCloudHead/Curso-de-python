#faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta necessario para pinta-la, sabendo que cada litro de tinta, pinta uma area de 2m²


altura = int(input('digite o valor de uma altura: '))
largura = int(input('digite o valor de uma largura de uma parede: '))
lata = int(2 ** 2)
parede = int(altura * largura * lata)
print(parede)