qtd = int(input("Informe a quantidade de pontos de água na amostra: "))
if (qtd <= 10):
    print("O tipo de solo, presente na amostra, é ROCHOSO!!!")
elif ((qtd > 10) and (qtd <= 40)):
    print("O tipo de solo, presente na amostra, é FIRME!!!")
elif ((qtd > 40) and (qtd <= 80)):
    print("O tipo de solo, presente na amostra, é PANTANOSA!!!")
else:
    print("QUANTIDADE INVÁLIDA!!!")