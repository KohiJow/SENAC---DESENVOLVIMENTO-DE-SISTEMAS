#EXEMPLO: Tratando o item a ser removido com if

mobile = ['MOTO G6', 'MOTO G7', 'MOTO G8']
qtd =    [100,        200,       300]

prod_ma_v = max(qtd)
prod_me_v = min(qtd)

produtos = prod_ma_v and prod_me_v

if prod_ma_v < prod_me_v:
    print(f'O produto com venda em nível ÓTIMO foi{produtos}')
elif prod_ma_v < prod_me_v:
    print(f'O produto com venda em nível BOM foi: {produtos}')
else:
    print(f'O produto com venda em nível RUIM foi: {produtos}')
