#Crie um programa que leia vários números inteiros pelo teclado. O prgrama só vai parar quando o usuario digitar o valor 999, que é a condição de parada. No final, mostre quantos numeros foram digitados e qual foi a soma entre eles (desconsiderando o flag)


#Minha primeira tentativa: 

listas_total = [] 
usuario = None 
print('Esse é o guarda números!') 
while usuario != 999: 
    print('Caso deseje encerrar digite: (999)') 
    print('Adicione números na lista!') 
    try: 
        usuario = int(input('Digite o número que deseja adicionar: ')) 
        listas_total.append(usuario) 
    except ValueError: 
        print('Digite apenas números') 
        
        
listas_total.remove(999) 
print(f'O total de númeoros adicionados na lista foram: {listas_total}')


#Minha segunda tentativa:

listas_total = [] 
usuario = None 
print('Esse é o guarda números!') 
while usuario != 999: 
    print('Caso deseje encerrar digite: (999)') 
    print('Adicione números na lista!') 
    try: 
        usuario = int(input('Digite o número que deseja adicionar: ')) 
        if usuario == 999: 
            listas_total = listas_total.remove(999) 
        else: 
            listas_total.append(usuario) 
    except ValueError: 
            print('Digite apenas números') 
            
            
print(f'O total de númeoros adicionados na lista foram: {listas_total}') 
print(f'Ao todo foram digitados o total de {len(listas_total)} números') 
print(f'A soma dos valores dentro da lista é: {sum(listas_total)}')


#Minha terceira tentativa:

listas_total = []
usuario = None

print('Esse é o guarda números!')
while usuario != 999:
    print('Caso deseje encerrar digite: (999)')
    print('Adicione números na lista!')
    try:
        usuario = int(input('Digite o número que deseja adicionar: '))
        if usuario != 999:
            listas_total.append(usuario)
    except ValueError:
        print('Digite apenas números')

    


print(f'O total de númeoros adicionados na lista foram: {listas_total}')
print(f'Ao todo foram digitados o total de {len(listas_total)} números') #(len) mostra a quantidade total de itens dentro da lista)
print(f'A soma dos valores dentro da lista é: {sum(listas_total)}') #(sum) soma os itens dentro da lista)



#Resolução do professor:


núm = cont = soma = 0
núm = int(input('Digite um número [999 para parar]: '))
while núm != 999:
    soma += núm
    cont += 1
    núm = int(input('Digite um número [999 para parar]: '))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')





#Desafio extra: Trocar a lista por contador += 1 e soma_num += usuario (Em termos de eficiencia e economia de mémoria usar as variáveis em exercicios como esses é mais profissional.
#porque como o exercício não pede pra guardar todos os números e sim pra somalos, usar variável em cez de lista consome menos mémoria.)

