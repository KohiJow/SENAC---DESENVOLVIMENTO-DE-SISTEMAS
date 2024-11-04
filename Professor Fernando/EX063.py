#Exercicio 3º - Tuplas no Python

#Lista para armazenar os clientes
clientes = []

def adicionar_cliente(nome, telefone, email):
    #Criando uma tupla para armazenar as informações do cliente
    cliente = (nome, telefone, email) #A tupla 'cliente' contém (nome, telefone, email)
    clientes.append(cliente) #Adicionando a tupla á lista de clientes
    
def exibir_clientes():
    for cliente in clientes: #Iterando sobre a lista de clientes
        nome, telefone, email = cliente
        print(f'Nome: {nome}, Telefone: {telefone}, E-mail: {email}') #Exibindo as informações do cliente
        
#Adicionando clientes
adicionar_cliente('José', '1234-5678', 'jose@email.com') # 'José' é adicionado como uma tupla
adicionar_cliente('Maria', '8765-4321', 'maria@email.com') # 'Maria' também é adicionado como uma tupla

#Exibindo clientes cadastrados
exibir_clientes()
