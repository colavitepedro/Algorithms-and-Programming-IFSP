import sys
print("(A) para carro movido à Álcool e (G) para movido à Gasolina!!!")
tc = input("Informe o tipo do carro: ").upper()

if ((tc != "A") and (tc != "G")):
    print("Código do tipo de carro inválido!")
    sys.exit()

ct = float(input("Informe a capacidade do tanque de combustível: "))

if (tc == "A"):
    print(f"Álcool e capacidade igual a {ct:,.2f} litros.")
else:
    print(f"Gasolina e capacidade igual a {ct:,.2f} litros.")

preco = float(input("Informe o valor do litro da gasolina: R$"))

valor = preco * ct

print(f"O valor necessário para encher o tanque de combustível é R${valor:,.2f}")