'''
4. Analise de Faturas
Você é responsável por analisar as faturas de clientes de uma empresa. Cada fatura tem o valor total, o número de parcelas, e o valor pago até o momento.

Tarefa: Crie uma função que verifique quais clientes ainda não quitaram suas faturas (valor pago é menor que o valor total).
'''

def verificar_faturas(faturas):
    return [cliente for cliente, (total, parcetas, pago) in faturas if pago < total]

# Exemplo de uso
faturas_clientes = [
('Afonso Ribeiro', (1000, 10, 500) ),
('Amanda Costa', (500, 5, 500)),
('Natália Correa', (750, 6, 600) ),
]

linha = '--------------------------------------------------------------------------------------------------'
print('\n' + linha + '\n Os clientes com os maiores DEBITOS sao:',verificar_faturas(faturas_clientes))
print(linha + "\n")
