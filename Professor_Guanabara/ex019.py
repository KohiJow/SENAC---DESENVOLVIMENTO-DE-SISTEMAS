#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele
#lendo o nome deles e escrevendo o nome do escolhido.

import random # Importa a biblioteca random
Alunos = ['Pedrinho', 'Gustavinho', 'Luisinho', 'Joãozinho'] #Lista os alunos da sala com o []]
print(random.choice(Alunos)) #Printa uma escolha randômica entre os alunos da lista