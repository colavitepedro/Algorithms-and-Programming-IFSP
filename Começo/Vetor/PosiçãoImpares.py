vetor = [0]*5

for i in range (0, 5):
    vetor[i] = int(input(f'Informe um número para a posição {i}°: '))

for i in range (1, 5, 2):
    print(f'[{vetor[i]}]', end = "  ")

for i in range (0, 5):
    if (i % 2 != 0):
        print(f'[{vetor[i]}]', end = "  ")
