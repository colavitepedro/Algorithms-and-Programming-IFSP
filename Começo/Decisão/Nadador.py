nome = input('Informe o nome do nadador: ')
idade = int(input('Informe a idade do nadador: '))

if ((idade >= 5) and (idade <= 7)):
    categoria = "Infantil A"

elif ((idade >= 8) and (idade <= 11)):
    categoria = "Infantil B"

elif ((idade >= 12) and (idade <= 13)):
    categoria = "Juvenil A"

elif ((idade >= 14) and (idade <= 17)):
    categoria = "Juvenil B"

elif (idade >= 18):
    categoria = "Adulto"

else:
    print("CATEGORIA INVÁLIDA!!!")

print(f"O nadador {nome}, de {idade} anos, está na categoria {categoria}!!!")