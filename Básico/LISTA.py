def espaco(a):
    for i in range(a):
        print('---------------------------------------------------------------')

lista1 = ['Abacate','Morango', 'Melancia', 'Banana', 'Goiaba', 'Figo', 'Melão']
lista1.append('Abacaxi') 
print(lista1) 

espaco(1)

print(lista1[1]) 

espaco(1)

lista1.insert(0, 'Kiwi')
print(lista1)            

espaco(1)

lista1.pop()
print(lista1)

espaco(1)

del lista1[2] 
print(lista1)

espaco(1)

lista1.remove('Kiwi')
print(lista1)

espaco(1)

print(lista1.count('Banana')) 
lista1.append('Banana')
print(lista1.count('Banana'))
lista1.remove('Banana')

espaco(1)
print(f'antes do .reverse {lista1}')
lista1.reverse() 
print(f'depois do .reverse {lista1}')

espaco(1)

print(f'antes do .sort {lista1}')
lista1.sort()          
print(f'depois do .sort {lista1}')

espaco(1)

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
dobronumeros = []

for numero in numeros:
    dobronumeros.append(numero * 2)
dobronumeros.clear()

espaco(1)

dobronumeros = [numero * 2 for numero in numeros]
print(dobronumeros)

espaco(1)

nomes = ['Pedro', 'Nicolau', 'Valentina', 'Sirlei', 'Nick']
nomes_maisculos = [nome.upper() for nome in nomes if nome[0] == 'N']
print(nomes)
print(nomes_maisculos)

espaco(1)

