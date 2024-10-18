import tkinter as tk

# Criar a classe do Calculator para Teste
class Calculator:
    def __init__(self):
        self.expression = ""

    def click(self, value):
        if value == "=":
            try:
                self.expression = str(eval(self.expression))
            except Exception:
                self.expression = "Erro"
        elif value == "C":
            self.expression = ""
        else:
            self.expression += str(value)

    def get_screen(self):
        return self.expression
# Fim da classe para teste

def create_gui():
    # Instancia a classe Calculator criada
    calc = Calculator()
    root = tk.Tk()
    root.title("Calculadora - PyCPhone")
    root.geometry("400x500")
    root.config(bg="#F0F0F0")

    screen = tk.StringVar()

    entry = tk.Entry(root, textvar=screen, font="Arial 24", bd=10, insertwidth=2, width=14, justify='right')
    entry.pack(fill="both", ipadx=8, padx=10, pady=20)

    buttons = [
        ["7", "8", "9", "/"],
        ["4", "5", "6", "*"],
        ["1", "2", "3", "-"],
        ["C", "0", "=", "+"]
    ]

    # Função que trata os cliques nos botões
    def button_click(event):
        text = event.widget.cget("text")
        calc.click(text)  # Passa o texto para a classe Calculator
        screen.set(calc.get_screen())  # Atualiza a tela com o valor da expressão

    def create_button(frame, text, color="#FFFFFF", bg="#C0C0C0"):
        button = tk.Button(frame, text=text, font="Arial 20", padx=20, pady=20, bg=bg, fg=color, borderwidth=0)
        button.pack(side="left", expand=True, fill="both", padx=5, pady=5)
        button.bind("<Button-1>", button_click)  # Usa button_click ao invés de click
        return button

    for row in buttons:
        frame = tk.Frame(root, bg="#F0F0F0")
        frame.pack(expand=True, fill="both")

        for button_text in row:
            if button_text in ["+", "-", "*", "/", "="]:
                create_button(frame, button_text, color="#FFFFFF", bg="#FFA500")
            elif button_text == "C":
                create_button(frame, button_text, color="#FFFFFF", bg="#FF6347")
            else:
                create_button(frame, button_text)

    root.mainloop()

if __name__ == "__main__":
    create_gui()
