voto = 0
c1 = 0
c2 = 0
c3 = 0
nulo = 0
branco = 0
quantidade_votos = 0


canditado1 = input('Informe o nome do Canditado 1: ')
canditado2 = input('Informe o nome do Canditado 2: ')
canditado3 = input('Informe o nome do Canditado 3: ')
print('')

print(f'1 - para {canditado1}; 2 - para {canditado2}; 3 - para {canditado3}')
print(f'4 - para voto em Branco e 5 - para voto Nulo')
print(f'***** -1 para encerrar a eleição *****')
print(f'')

while voto != -1:
    quantidade_votos += 1
    voto = int(input('DIGITE SUA ESCOLHA: '))
    if voto == 1:
        c1 += 1
    elif voto == 2:
        c2 += 1
    elif voto == 3:
        c3 += 1
    elif voto == 4:
        branco += 1
    elif voto == 5:
        nulo += 1
    elif voto > 5 and voto < -1:
        print('Código Inválido')
        quantidade_votos = quantidade_votos - 1
    elif voto == -1:
        quantidade_votos = quantidade_votos - 1
        print('***** ELEIÇÃO ENCERRADA *****')
print('')

if (c1 == c2 or c1 == c3 or c2 == c3) and branco != quantidade_votos and nulo != quantidade_votos:
    vencedor = "Empate"
elif branco == quantidade_votos and nulo == quantidade_votos:
    vencedor = "Eleição Inválida"
elif c1 > c2 and c1 > c3:
    vencedor = canditado1
elif c2 > c1 and c2 > c3:
    vencedor = canditado2
elif c3 > c1 and c3 > c2:
    vencedor = canditado3


if vencedor == "Empate":
    print(f'Houve um empate entre os canditados.')
    print(f'{c1} voto(s) em {canditado1}, {c2} voto(s) em {canditado2}, {c3} voto(s) em {canditado3}.')
    print(f'{branco} voto(s) em branco e {nulo} voto(s) nulo.')
    print(f'Total de {quantidade_votos} eleitor(es)')

elif vencedor == "Eleição Inválida":
    print(vencedor)
    print(f'{c1} voto(s) em {canditado1}, {c2} voto(s) em {canditado2}, {c3} voto(s) em {canditado3}.')
    print(f'{branco} voto(s) em branco e {nulo} voto(s) nulo.')
    print(f'Total de {quantidade_votos} eleitor(es)')

else:
    print(f'{vencedor} ganhou as eleições!!!')
    print(f'{c1} voto(s) em {canditado1}, {c2} voto(s) em {canditado2}, {c3} voto(s) em {canditado3}.')
    print(f'{branco} voto(s) em branco e {nulo} voto(s) nulo.')
    print(f'Total de {quantidade_votos} eleitor(es)')