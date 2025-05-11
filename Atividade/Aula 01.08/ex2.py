nomes = [0]*5
medias = [0.0]*5
maior_media = 0.0
maior_mediaNOME = ''
for i in range(5):
    nomes[i] = input(f'Informe o nome do {i + 1}º aluno: ')

for i in range(5):
    medias[i] = float(input (f'Informe a média do aluno {nomes[i]}: '))

for i in range(5):
    if medias[i] > maior_media:
        maior_media = medias[i]
        maior_mediaNOME = nomes[i]

print()
print(f'A maior média é {maior_media} do aluno {maior_mediaNOME}')