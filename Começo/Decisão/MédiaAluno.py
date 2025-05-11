nome = input("Informe o nome do aluno: ")
n1 = float(input("Informe a primeira nota: "))
n2 = float(input("Informe a segunda nota: "))
media = (n1 + n2) / 2

if (media >= 6):
    situacao = "Aprovado"
elif ((media >= 4) and (media < 6)):
    situacao = "de Recuperação"
else:
    situacao = "Reprovado"

print(f"{nome}, a sua média é {media} e você está {situacao}")