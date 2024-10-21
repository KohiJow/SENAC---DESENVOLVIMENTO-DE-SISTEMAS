#Exemplo 24 - While verifica dia da semana

semana = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira']
i = 0
while semana:
    if i == 3:
        print('\n' + ' -- Um dia antes do famoso SEXTOU é:', semana[i])
        break
    i += 1 # Contador de 0 até 3