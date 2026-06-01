#While com condição para interromper, porém sem break:
cont = 1
while cont <= 10:
    print(cont, ' -> ', end='')
    cont += 1
print('Acabou')


#while que mantem em laço enquanto n for diferente se 999 também uma forma de interromper sem break:
n = 0
while n != 999:
    n = int(input('Digite um número: '))
print(n)


#while com input e condição de contador para interromper: 
n = cont = 0
while cont < 5:
    n = int(input('Digite um número: '))
    cont += 1
print(n)


#while com interrupção 'quebra galho', dessa forma o flag sendo 999 ainda está sendo contado pelo python e essa forma de interrupção passa pelo print porém não passa pelo teste lógico;
n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print(f'A soma vale {s}')


#while com interrupção usando break:
#Forma mais comum e relativamente correta de se interromper laços em um while onde seguindo o teste lógico, se n for igual a 999 então interrompa, fazendo com que assim o python entenda 999 como uma flag de fato.
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print(f'A soma vale {s}')








