#pip  install pytest 
import pytest #importa pytest
from app import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_addition(calculator):
    assert calculator.evaluate_expression("2+2") == 4
    
def test_subtraction(calculator):
    assert calculator.evaluate_expression("5 - 2") == 3
        
#python -m pytest (Nome do Arquivo).py