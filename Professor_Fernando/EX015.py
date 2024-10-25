'''
Veja que exemplo bacana, os caracteres =, - e > representam os eixos de 
formatação de espaços e preenchimento dos espaços de cada coluna da função
format é nativa da linguagem Python, aplicada a formatação de Strings, repare na saída deste algoritmo, utilizando a função "format"
faça modificações no algorítmo e teste outras possibilidades de formatação.
'''
print('{0:=<8} | {1:-^8} | {2:.>8}'. format('Menor:', 'Médio:', 'Grande:'))
print('{0:=<8} | {1:-^8} | {2:.>8}'. format(100, 200, 300))
