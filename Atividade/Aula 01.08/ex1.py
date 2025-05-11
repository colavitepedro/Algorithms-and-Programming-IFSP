vetor = [0]*20

for i in range (10):
    vetor[i] = int(input('Informe um número para o vetor: '))

for i in range (10):
    vetor[10 + i] = vetor [9 - i]

for i in range(20):
    if i != 0:
        print(' - ', end='')
    print(vetor[i], end='')
print()