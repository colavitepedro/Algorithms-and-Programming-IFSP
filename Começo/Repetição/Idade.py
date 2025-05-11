maior = 0
menor = 0
somaidade = 0
n = int(input('Informe a quantidade de pessoas: '))
for i in range (1, n + 1):
    idades = int(input('Informe a idade: '))
    somaidade += idades
    if (idades > maior):
        maior = idades
    if (idades < menor):
        menor = idades
    elif (menor == 0):
        menor = idades
    media = somaidade / n
print(f'Foram consultadas {n} pessoa(s), sendo {maior} a maior idade, {menor} a menor idade e {media:,.2f} a média da(s) idade(s)!')