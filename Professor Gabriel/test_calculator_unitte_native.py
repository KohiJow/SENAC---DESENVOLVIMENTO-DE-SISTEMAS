import unittest #importa a biblioteca para testes
from app import Calculator #Importa a classe calculator

#Define uma nova classe de teste, no qual herda as funções do Unitest
class TestCalculatorLogic(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()#cria a instancia da Calculadora
    def test_addition(self):
        self.assertEqual(self.calculator.evaluate_expression('2+2'), 4)
        
#Executa os testes, terminal (diretamente)        
if __name__ == '__main__':
    unittest.main()
    
    #Executando!!!!
    # ---> python -m unittest test_calculator.py <---