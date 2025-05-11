def espaco(a):
    for i in range(a):
        print('---------------------------------------------------------------')

lista = ['Um', 'Dois', 'Três'] 
print(lista[0])                

espaco(1)

dicionario = {'nome':'Pedro', 'idade': 18, 'time':'Corinthians','remover':'sei lá'}
print(dicionario['nome'])
print(dicionario['idade']) 
print(dicionario['time'])
print()

espaco(1)

print(dicionario.get('nome'))
print(dicionario.get('idade'))
print(dicionario.get('time'))
print()

espaco(1)

print(dicionario) 
dicionario.pop('remover') 
print(dicionario) 

espaco(1)

print(dicionario.keys()) 
print(dicionario.values()) 

espaco(1)

dicionario.clear() 
print(dicionario)

espaco(1)

pessoa = {
    'nome': 'Pedro',
    'idade': 18,
    'time': 'Corinthians',
    'interesses': ['Gatos','Liverpool','Laranja'], 
    'pet': { 
        'nome': 'Nick',
        'idade': '6 meses',
        'cor':'Preto e branco',
        'raça': 'Maine coon' 
    }
}

print(pessoa)
espaco(1)

print(pessoa.get('nome'))
print(pessoa.get('interesses'))
print(pessoa.get('interesses')[0])
print(pessoa['interesses'][1]) 
print()
print(pessoa.get('pet'))
print(pessoa.get('pet').get('nome'))
print(pessoa['pet']['nome']) 
print()
espaco(1)

pessoa['ano_nascimento'] = 2006 
print(pessoa) 
pessoa['cores_favoritas'] = ['Laranja', 'Preto', 'Branco']
pessoa['namorada'] = { 
    'nome': 'Valentina',
    'idade': 18,
    'time': 'Corinthians'
}
print(pessoa)

espaco(1)

print(pessoa.get('namorada').get('nome'))