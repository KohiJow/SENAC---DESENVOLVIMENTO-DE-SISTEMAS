#Exercicio 2 - Dicionários no Python

agenda = {}

def adicionar_contato(nome, telefone):
    agenda[nome] = telefone

def remover_contato(nome):
    if nome in agenda:
        del agenda[nome]

def buscar_contato(nome):
    telefone = agenda.get(nome)
    if telefone:
        return f"O telefone encontrado foi: {telefone}"
    else:
        return "Contato não encontrado"

def exibir_contato():
    for nome, telefone in agenda.items():
        print(f"Nome> {nome}, Telefone: {telefone}")

#Teste

adicionar_contato('Fernando', '1234-5678')
adicionar_contato('Ana','8765-4321')
remover_contato('Ana')
print(buscar_contato('Fernando')) #Exibe a mensagem com o telefone
exibir_contato() #Exibe todos os contatos
