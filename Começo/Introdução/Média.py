#Programa que recebe o sálario vase de yum funcionário.
#Calcule e mostre o salário a receber, sabendo que esse funcionário term gratificação de R$50,00
# E paga imposto de 10% sobre o salário base


sal = float(input("Informe o salário do funcionário: R$"))
desc = sal * 1/10
salfinal = sal + 50 - desc
print(f"O salário final do funcionário é R${salfinal:.2f}")