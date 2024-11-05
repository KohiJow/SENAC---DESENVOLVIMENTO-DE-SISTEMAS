'''
Exercício nº0

O primeiro passo é instalar a biblioteca Tkinter no windows ou linux,
utilizando o comando --> pip instalar tk --> no terminal do VsCode ou Anaconda.

Execute os comandos a seguir e aumente e Maximize a janela e configura o resultado.
''''''
import tkinter as tk #Esta forma importa TODAS as opções da biblioteca do Tkinter

janela = tk.Tk()
janela.title('SCM - (Sistema de Cotação de Moedas)')

msg0 = tk.Label(text='Sistema de Cotação de Moedas')
msg0.pack()

msg1 = tk.Label(text='Selecione o tipo de moeda:')
msg1.pack()

janela.mainloop( )
'''
'''
import tkinter as tk #Esta forma importa TODAS as opções da biblioteca do Tkinter

janela = tk.Tk()
janela.title('SCM - (Sistema de Cotação de Moedas)')

msg0 = tk.Label(text='> Sistema de Cotação de Moedas <', fg= 'white', bg='#7E40C8', width=50, height=10)
msg0.pack()

msg1 = tk.Label(text='Selecione o tipo de moeda: (D = Dólar, E= Euro, R= Reais)', width=70,height=15)
msg1.pack()

moeda = tk.Entry()
moeda.pack()

janela.mainloop()
'''

import tkinter as tk #Esta forma importa TODAS as opções da biblioteca do Tkinter

janela = tk.Tk()
janela.title('SCM - (Sistema de Cotação de Moedas)')

msg0 = tk.Label(text='> Sistema de Cotação de Moedas <', fg='White', bg='#7E40C8')
msg0.grid(row=0, column=0, columnspan=2, sticky='NSEW')

msg1 = tk.Label(text='Selecione o tipo de moeda:')
msg1.grid(row=1, column=0)

dicionario_cotacoes = {
    'Dólar': 4.99,
    'Euro': 6.29,
    'Real': 4.00
}

botao = tk.Button(text='Buscar Cotação')
botao.grid(row=2, column=1)

moeda = tk.Entry()
moeda.grid(row=1, column=1)


janela.mainloop( )
