vet = [0]*5

for cont in range (0, 5, 1):
    vet[cont] = int(input(f"Informe o número para a posição {cont + 1}: "))

for cont in range (0, 5, 1):
    print(f"[{vet[cont]}]", end = '  ') 