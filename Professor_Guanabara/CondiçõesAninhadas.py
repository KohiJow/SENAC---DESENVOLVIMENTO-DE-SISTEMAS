nome = str(input('Qual é seu nome?'))

if nome == 'Jow':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem comum no brasil ')    
else:
    print('Que nome normal...')
print(f'Tenha um bom dia! {nome}')