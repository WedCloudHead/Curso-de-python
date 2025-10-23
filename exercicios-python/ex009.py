#faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada


num = int(input('digite um numero qualquer:'))
tab = (num * 1, num * 2, num * 3, num * 4, num * 5, num * 6, num * 7, num * 8, num * 9, num * 10)
res = ('a tabuada de {} é: {} '.format(num, tab))
print(res)