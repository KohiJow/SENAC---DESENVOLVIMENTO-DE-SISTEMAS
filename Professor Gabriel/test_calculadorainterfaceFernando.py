import pytest
from calculadoraFernando import Calculator

@pytest.fixture
def calc():
    #Cria a instancia da classe calculator para cada teste
    return Calculator()

#Clique de adição
def test_addition(calc):
    calc.click("1")
    calc.click("+")
    calc.click("2")
    calc.click("=")
    #verifica se o resultado na tela é "3"
    assert calc.get_screen() == "3"
    
    #Testa função de limpar
def test_clear(calc):
    calc.click("5")
    calc.click("C")
    assert calc.get_screen() == ""
    