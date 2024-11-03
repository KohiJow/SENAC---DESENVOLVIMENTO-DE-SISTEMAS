'''
3. Cadastro de Participantes de um Evento
Você está organizando um evento e tem uma lista com o nome de todos os participantes.

Tarefa: Crie uma função que:
Verifique se uma pessoa está na lista de participantes.
Retorne o número total de participantes.
'''

def gerenciar_participantes(participantes, nome) :
    if nome in participantes:
        return f'{nome} esta na lista de participantes.'
    else:
        return f'{nome} não esta na lista de participantes.', f'Total de participantes: {len(participantes)}'

# Estudo de caso
lista_participantes = ['João', 'Maria', 'Pedro', 'Ana']
print(gerenciar_participantes(lista_participantes, 'Ana') ) # Saida: 'Ana esta na lista de participantes.'
print(gerenciar_participantes(lista_participantes, 'Lucas') ) # Saída: 'Lucas não esta na lista de participantes.'
