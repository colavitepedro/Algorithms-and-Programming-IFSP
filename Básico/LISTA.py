def espaco(a):
    for i in range(a):
        print('---------------------------------------------------------------')

lista1 = ['Abacate','Morango', 'Melancia', 'Banana', 'Goiaba', 'Figo', 'Melão']
lista1.append('Abacaxi') # .append adiciona um elemento a lista, o .append adiciona sempre na última posição da lista
print(lista1) 

espaco(1)

print(lista1[1]) # da para usar apenas um índice o colando entre []

espaco(1)

lista1.insert(0, 'Kiwi') # .insert adiciona um elemento a tabela em um determinado lugar/índice 
print(lista1)            # (índice que vai ser colocado, nome do elemento) --> estrutura do .insert

espaco(1)

lista1.pop() # .pop exclui o último elemento da lista
print(lista1)

espaco(1)

del lista1[2] # comando del + nome da lista + [índice] --> apaga o elemento do índice correspondente
print(lista1)

espaco(1)

lista1.remove('Kiwi') # nome da lista + .remove + ('nome do elemento') --> apaga o elemento baseado no valor do elemento
print(lista1)

espaco(1)

print(lista1.count('Banana')) # lista + .count + ('elemento') --> conta quantos vezes esse 'elemento' aparece na lista
lista1.append('Banana')
print(lista1.count('Banana'))
lista1.remove('Banana')

espaco(1)
print(f'antes do .reverse {lista1}')
lista1.reverse() #inverte a ordem dos elementos da lista
print(f'depois do .reverse {lista1}')

espaco(1)

print(f'antes do .sort {lista1}')
lista1.sort()           # organiza a lista em ordem alphanumeric
print(f'depois do .sort {lista1}')

espaco(1)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dobronumeros = []

for numero in numeros:
    dobronumeros.append(numero * 2)
dobronumeros.clear()

espaco(1)

dobronumeros = [numero * 2 for numero in numeros] # novalista = [expressão + for + item + in + lista]
print(dobronumeros)

espaco(1)

nomes = ['Pedro', 'Nicolau', 'Valentina', 'Sirlei', 'Nick']
nomes_maisculos = [nome.upper() for nome in nomes if nome[0] == 'N'] # novalista = [expressão + for + item + in + lista + condição]
print(nomes)
print(nomes_maisculos)

espaco(1)

