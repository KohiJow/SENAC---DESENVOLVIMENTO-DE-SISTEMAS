'''
#Exemplo: Programa de abertura do arquivo.txt

with open('arquivo.txt', 'r') as file_object:
    texto = file_object.read()
    print(texto)
'''

#Exemplo: Programa de abertura do arquivo.txt: Try e Expect

try:
    arquivo = open('arquivo.txt')
except FileNotFoundError as erro:
    print(f'O arquivo .TXT não foi encontrado no diretório de projetos\n'
          f'{erro}')   


with open('arquivo.txt', 'r') as file_object:
    texto = file_object.read()
    print(texto)