#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo
#calcule e mostre o comprimento da hipotenusa.
#from math import sqrt
#cateto_oposto = float(input('Insira o valor do cateto oposto: '))
#cateto_adjacente = float(input('Insira o valor do cateto adjascente: '))
#hipotenusa = (cateto_adjacente * cateto_adjacente) + (cateto_oposto * cateto_oposto)
#resultado = sqrt(hipotenusa)

#print(f'O comprimento da hipotenusa do triângulo retângulo é {resultado:.2f}')

from math import sqrt #o from importa de matemática apenas o sqrt que é a raiz quadrada

opposite_side = float(input('Insert the value of the opposite side: ')) #Um input de um dos catetos para calcular a hypotenusa
adjacent_side = float(input('Insert the value of the adjascent side: '))
hypotenuse = (opposite_side * opposite_side) + (adjacent_side * adjacent_side) #fórmula para saber o resultado
Result = sqrt(hypotenuse) #raiz quadrada
print(f'The result of hypotenuse is {Result}')
