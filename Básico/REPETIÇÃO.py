def envia_email(cliente):
    print(f'Email enviado para o cliente {cliente}!')
clientes = ['Pedro', 'Valentina', 'Markus', 'Felipe']
for cliente in clientes:
    envia_email(cliente)

print()
print()

for i, cliente in enumerate(clientes):
    if i == 3:
        break # o "break" para a execução na hora em que a condição se torna verdadeira!!!
    envia_email(cliente)
print()
print()

for i, cliente in enumerate(clientes):
    if i == 1:
        continue # o "continue" pula um item da execução
    envia_email(cliente)
print()
print()

for i in range(10):
    print(i)

print()
print()

numero = 1
while numero > 0:
    print(numero)
    numero += 1
    if numero == 5:
        continue
    if numero == 11:
        break
    