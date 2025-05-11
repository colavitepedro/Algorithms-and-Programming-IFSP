
menu = 0
somasalario = 0
somafilhos = 0
contador = 0
maior_salario = 0
cem = 0

while menu != 2:
    print('1 - Cadastro ||| 2 - Encerrar')
    menu = int(input('Informe o código do menu: '))
    print('')

    if menu == 1:
        filhos = int(input('Informe o número de filhos: '))
        salario = float(input('Informe o salário: R$'))
        print('')
        somasalario += salario
        somafilhos += filhos
        contador += 1

        if salario > maior_salario:
            maior_salario = salario

        if salario <= 100:
            cem += 1

        if menu > 2:
            print('Opção Inválida')
            contador = contador - 1

    elif menu == 2:
        print('Cadastro Encerrado!')
        
    else:
        print('Código Inválido')

print('')
if contador > 0:
    media_salario = somasalario/contador
    media_filhos = somafilhos/contador
    percentual_cem = (cem/contador)*100
    print(f'A média dos salários é R${media_salario:,.2f}')
    print(f'A média do número de filhos é {media_filhos:,.2f}')
    print(f'O maior salário é de R${maior_salario:,.2f}')
    print(f'{percentual_cem:,.2f}% tem um salário de até R$100,00')
    print('')
else:
    print('KKKKKKKKKKKKKKKK')