def maior(maior_numero, n1):
    if maior_numero < n1:
        maior_numero = n1
    return maior_numero

def menor(menor_numero, n1):
    if menor_numero > n1:
        menor_numero = n1
    return menor_numero

print()
n1 = int(input('Informe um número: '))
for i in range (4):
    n = int(input('Informe um número: '))

print()
print(f'O maior número é: {maior(n, n1)}')
print(f'O menor número é: {menor(n, n1)}')