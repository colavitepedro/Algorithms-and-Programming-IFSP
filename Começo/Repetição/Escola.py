somaidade = 0
qtd = 20
mulher = 0
maior = 0

for i in range (0, qtd):
    idade = int(input(f'Informe a idade do {i + 1}° candidato: '))
    sexo = input('F para Feminino e M para Masculino: ').upper()
    print('')
    somaidade += idade
    media = somaidade / qtd
    if (sexo == 'F'):
        mulher += 1
    if (idade >= 18):
        maior += 1
    if (i == qtd - 1):
        print("TURMA LOTADA!!!")
        print('')

print(f'A média das idades dos inscritos é {media:.2f}.')
print(f'Há {mulher} inscrito(s) que são do sexo FEMININO.')
print(f'Há {maior} inscrito(s) que são MAIOR(ES) DE IDADE.')
