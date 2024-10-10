class Calculator:
    #Metodo para avaliar a expressão matemática
    #passada como string

    def evaluate_expression(self, expression):
        try:
            result = eval(expression) #tenta calcular o resultado da expressão
            return result #retorna o Resutado
        except Exception:
            return 'erro' #se tiver erro(Ex: Divisão por Zero) mostra errp
        
#Exemplos para os testes utilizando (unittest e pytest)
if __name__ == '__main__':
    calc = Calculator() #cria a instacia da calculadora
    #Expressões, testes e lógicas
    print(calc.evaluate_expression('2 + 2')) #saida 4
    print(calc.evaluate_expression('10 / 0'))#saida erro
    print(calc.evaluate_expression('5 * 6'))#saida 30
    
#app.mainloop()
    