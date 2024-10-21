#Exemplo 7 - For listando tabela de endereço IP de 192.168.0.1 até 192.168.0.10
ip = [1,2,3,4,5,6,7,8,9,10]
msg = '192. 168.0. '
for lista, indices in enumerate (ip):
    print(msg + format (indices) )
#Fim do código

