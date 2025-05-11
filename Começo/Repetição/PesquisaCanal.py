nove = 0
doze = 0
tres = 0
quarenta = 0
outros = 0
total = 1
canal = 1
while canal != 0:
    canal = int(input('Informe o Canal (9, 12, 23 ou 40): '))
    if canal == 9:
        nove += 1
    elif canal == 12:
        doze += 1
    elif canal == 23:
        tres += 1
    elif canal == 40:
        quarenta += 1
    elif canal != 0 and canal != 9 and canal != 12 and canal != 23 and canal != 40:
        outros += 1

total = (nove + doze + tres + quarenta + outros)
nove = (nove/total)*100
doze = (doze/total)*100
tres = (tres/total)*100
quarenta = (quarenta/total)*100
outros = (outros/total)*100

print(f'Canal 9  = {nove:.2f}%')
print(f'Canal 12 = {doze:.2f}%')
print(f'Canal 23 = {tres:.2f}%')
print(f'Canal 40 = {quarenta:.2f}%')
print(f'Outros canais  = {outros:.2f}%')