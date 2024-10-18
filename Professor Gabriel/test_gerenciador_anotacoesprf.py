import pytest
from unittest.mock import patch, MagicMock
import tkinter as tk  #Adicione esta linha
from gerenciadordeanotacoesprf import add_note, delete_note  

@pytest.fixture
def setup_listbox():
    listbox = MagicMock()
    return listbox

def test_add_note(setup_listbox):
    with patch('tkinter.simpledialog.askstring', return_value='Test Note'):
        add_note(setup_listbox)
        setup_listbox.insert.assert_called_once_with(tk.END, 'Test Note')  #Agora 'tk' está definido

def test_add_note_simulation(setup_listbox):
    #Teste para verificar a inclusão de uma nota.
    note_content = 'Adicionar Nota'
    with patch('tkinter.simpledialog.askstring', return_value=note_content):
        add_note(setup_listbox)
        setup_listbox.insert.assert_called_once_with(tk.END, note_content)  #Verifica se a nota foi adicionada

def test_delete_note_success(setup_listbox):
    setup_listbox.curselection.return_value = [0]  #Simula a seleção de uma nota
    delete_note(setup_listbox)
    setup_listbox.delete.assert_called_once_with(0)  #Verifica se a nota foi removida

def test_delete_note_no_selection(setup_listbox):
    setup_listbox.curselection.return_value = []  #Simula que nenhuma nota está selecionada
    with patch('tkinter.messagebox.showwarning') as mock_warning:
        delete_note(setup_listbox)
        mock_warning.assert_called_once_with("Aviso", "Nenhuma nota selecionada.")  #Verifica o aviso
