vetorA = [0]*10
vetorB = [0]*10

for i in range (10):
    vetorA[i] = int(input(f'Informe um valor para a posição {i + 1} do vetor A: '))

def mudar_vetor (vetorA, vetorB):
    for i in range(10):
        if vetorA[i] % 2 == 0:
             vetorB[i] = vetorA[i] * 5
        else:
            vetorB[i] = vetorA[i] + 3
    return vetorB[i]

mudar_vetor(vetorA,vetorB)

print()

print('VETOR ORIGINAL: ')
for i in range(10):
    if i != 0:
        print(' - ', end='')
    print(vetorA[i], end='')
print()

print('VETOR MODIFICADO: ')
for i in range(10):
    if i != 0:
        print(' - ', end='')
    print(vetorB[i], end='')
print()