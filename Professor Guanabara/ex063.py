# Solicita ao usuário que insira o número de termos da sequência de Fibonacci que ele deseja exibir.
n = int(input('Quantos termos vc quer mostrar?\n'))

# Inicializa o primeiro termo da sequência de Fibonacci com o valor 0.
t1 = 0

# Inicializa o segundo termo da sequência de Fibonacci com o valor 1.
t2 = 1

# Define o contador, começando em 3, pois os dois primeiros termos já estão definidos.
cont = 3

# Imprime os dois primeiros termos da sequência, separados por "->". O parâmetro 'end=" "' impede que a próxima linha seja quebrada.
print(f"{t1} -> {t2}", end=" ")

# Inicia o loop para calcular e exibir os próximos termos da sequência de Fibonacci.
while cont <= n:
    # Calcula o próximo termo da sequência somando os dois termos anteriores.
    t3 = t1 + t2

    # Exibe o próximo termo da sequência, mantendo o formato "->" entre os números.
    print(f"-> {t3}", end=" ")

    # Atualiza o valor de t1 para o valor de t2 (avanço na sequência).
    t1 = t2

    # Atualiza o valor de t2 para o valor de t3 (avanço na sequência).
    t2 = t3

    # Incrementa o contador para acompanhar a quantidade de termos exibidos.
    cont += 1

# Imprime "-> Fim" ao final da sequência para indicar que o programa terminou.
print("-> Fim")
