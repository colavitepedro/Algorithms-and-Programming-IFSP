n = 5
vetor = [0]* n
vetornovo = [0]* n

for i in range (0, n):
    vetor[i] = int(input(f'Informe um valor para a posição {i + 1}: '))

for i in range (0, n):
    if (i % 2 != 0):
        vetornovo[i] = (vetor[i] * 0.02) + vetor[i]
    else:
        vetornovo[i] = (vetor[i] * 0.05) + vetor[i]

for i in range (0, n):
    print(f'[{vetor[i]}]', end = "  ")

print(' ')

for i in range (0, n):
        print(f'[{vetornovo[i]}]', end = "  ")