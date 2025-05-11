def espaco(a):
    for i in range(a):
        print('---------------------------------------------------------------')

def somar(a, b):
    resultado = a + b
    return resultado
print(somar(10, 5))  

print(espaco(1))

def envia_email():
    email = 'aleatório@gmail.com'
    senha = '12345678'
    email_dest = 'zeca@gmail.com'
    #resto do código
    return 'email enviado!' 

pessoas = ['Pedro', 'Valentina', 'Markus', 'Felipe']
for pessoa in pessoas:
    email_enviado = envia_email()
    print(pessoa)
    print('Email enviado!!!')
    print()

def enviar_email(nome, email):
    return f'Email enviado para {nome}, dona do e-mail {email}'

galeras = [
    {
        'nome': 'Pedro',
        'email': 'pedro@gmail.com'
    },
    {
        'nome': 'Valentina',
        'email': 'valentina@gmail.com'
    },
    {
        'nome': 'Markus',
        'email': 'markus@gmail.com'
    },
    {
        'nome': 'Felipe',
        'email': 'felipe@gmail.com'
    }
]

print(espaco(1))

for galera in galeras:
    print(enviar_email(galera['nome'], galera['email']))
    print()