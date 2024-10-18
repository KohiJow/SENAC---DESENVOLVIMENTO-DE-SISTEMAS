import sys
from PyQt5 import QtWidgets, QtCore

class NoteManager(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Gerenciador de Notas")

        #Layout principal
        layout = QtWidgets.QVBoxLayout()

        #Lista de notas
        self.listbox = QtWidgets.QListWidget(self)
        layout.addWidget(self.listbox)

        #Botão para adicionar nota
        add_button = QtWidgets.QPushButton("Adicionar Nota", self)
        add_button.clicked.connect(self.add_note)
        layout.addWidget(add_button)

        #Botão para remover nota
        delete_button = QtWidgets.QPushButton("Remover Nota", self)
        delete_button.clicked.connect(self.delete_note)
        layout.addWidget(delete_button)

        self.setLayout(layout)

    def add_note(self):
        note, ok = QtWidgets.QInputDialog.getText(self, "Nota", "Digite a sua nota:")
        if ok and note: 
            self.listbox.addItem(note)

    def delete_note(self):
        selected_items = self.listbox.selectedItems()
        if not selected_items:
            QtWidgets.QMessageBox.warning(self, "Aviso", "Nenhuma nota selecionada.")
            return
        for item in selected_items:
            self.listbox.takeItem(self.listbox.row(item))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    note_manager = NoteManager()
    note_manager.resize(400, 300)
    note_manager.show()
    sys.exit(app.exec_())