#Exemplo 25 - While com uma condição VERDADEIRA: ''"

lo =  "--------------------------------------------------------"
while True:
    print(lo)
    valida_mundial = input ("O PALMEIRAS tem mundial? Sim ou Não -- > ")
    if valida_mundial == 'Sim':
        break
    else:
        print('\n' + 'CORRETO! O PALMEIRAS não tem Mundial :- )' + '\n')
