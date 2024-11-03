'''
2. Classificação de Alunos
Uma escola deseja classificar seus alunos em categorias "Aprovado", "Recuperação" e "Reprovado", com base em suas notas finais.

Tarefa: Crie uma função que, dado uma lista de alunos e suas notas, classifique cada aluno de acordo com as seguintes regras:
Nota >= 7: Aprovado
5 <= Nota < 7: Recuperaçao
Nota < 5: Reprovado
'''
def classificar_alunos(alunos) :
    # Classifica cada aluno conforme a nota
    classificacao = [(aluno, 'Aprovado' if nota >= 7 else 'Recuperação' if nota >= 5 else 'Reprovado' )
    for aluno, nota in alunos]
    return classificacao

# Estudo de caso
resultado = 'A LISTA DE ALUNOS APROVADOS E REPROVADOS'
linha = '-----------------------------------------------------------------------------------------'
print('\n' + linha + '\n' + resultado + '\n')
alunos_notas = [ ('Ana', 8), ('Bruno', 6.5), ('Carlos', 4), ('Daniela', 7.5)]
print(classificar_alunos(alunos_notas))
print(linha + '\n')
# Saída: [('Ana', 'Aprovado'), ('Bruno', 'Recuperação' ), ('C', '), ,)
