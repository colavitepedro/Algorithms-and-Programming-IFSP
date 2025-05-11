def soma(numero1, numero2):
    resultado = numero1 + numero2
    return resultado

n1 = int(input("Informe um valor: "))
n2 = int(input("Informe um valor: "))

print(f'{n1} + {n2} = {soma(n1,n2)}')