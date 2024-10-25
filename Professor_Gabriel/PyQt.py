#pip intall PyQt5 (cmd)
 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout
 
def greet ():
    label.setText('Olá, Mundo!') #atualiza o botão ao ser chamado
 
#Inicia a aplicação
app = QApplication(sys.argv)
 
#Cria a janela principal
window = QWidget()
window.setWindowTitle('Hello Word App!')
 
#Aqui informamos o layout vertical e organiza os widgets de forma sequencial
layout = QVBoxLayout()
 
#Widgets
 
#Rótulo vazio
label = QLabel('')
layout.addWidget(label)
 
#Botao que chama a função Greet
button = QPushButton('Clique aqui')
button.clicked.connect(greet)
layout.addWidget(button)
 
 
'''Obrigatórios:'''
 
#Define o layout da janela de acordo com o sistema operacional
window.setLayout(layout)
 
#Exibe a janela
window.show()
 
#Executa o loop da aplicação
sys.exit(app.exec_())