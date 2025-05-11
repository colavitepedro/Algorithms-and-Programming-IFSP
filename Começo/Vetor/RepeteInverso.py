i = 0
vetor = [0]*10

for i in range (0, 10, 1):
   vetor[i] = int(input('Informe um número: '))

for i in range (9, -1, -1):
    print(f'[{vetor[i]}]', end = "  ")