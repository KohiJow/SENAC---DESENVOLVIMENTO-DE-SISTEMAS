'''
Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonaro Brasileiro de Futebol, na ordem de colocacao. Depois mostre:
A) Apenas os 5 primeiros colocados.
B) Os ultimos 4 colocados da tabela.
C) Uma lista com os times em ordem alfabetica.
D) Em que posicao na tabela esta o time da Chapecoense.(???? n tem)
'''



os_20_colocados = ('null','Botafogo', 'Palmeiras', 'Flamengo', 'Fortaleza', 
                   'Internacional', 'Sao Paulo', 'Corinthians', 'Bahia',
                   'Cruzeiro', 'Vasco', 'Vitoria', 'Fluminense', 'Gremio', 
                   'Juventude', 'Red Bull Bragantino', 'Athletico-PR', 'Criciuma',
                   'Atletico-GO', 'Cuiaba')
os_20_colocados_abc= tuple(sorted(os_20_colocados))

print('--='*15)
print(f'A)Os primeiros 5 colocados: {os_20_colocados[1:6]}')
print('--='*15)
print('--='*15)
print(f'B)Os ultimos 4 colocados: {os_20_colocados[15:]}')
print('--='*15)
print('--='*15)
print(f'C)Em ordem alfabetica eles ficam {os_20_colocados_abc}')
print('--='*15)
print('--='*15)
print(f'Corinthians que ganhou do neymar ontem esta na {os_20_colocados.index("Corinthians")} posicao')