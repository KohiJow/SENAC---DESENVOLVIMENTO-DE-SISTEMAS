n1 =input("Enter a Number: ")
print("Qual o tipo primitivo desse valor? ", type(n1)) ##verifica o tipo da variável
print("Ele é numérico? ", n1.isnumeric()) ##verifica se é numérico
print("Ele é uma letra? " ,n1.isalpha()) ##verifica se é letra
print("Ele é uma letra e um número ?", n1.isalnum()) ##verifica se é letra e número
print("Ele só tem caractéres minúsculos? ", n1.islower()) ##verifica se só tem letras minúsculas
print("Ele só tem caracteres maiúsculos? ", n1.isupper()) ##verifica se só tem letras maiúsculas
print("Ele é Decimal?", n1.isdecimal()) ##verifica se é decimal
print("Ele é printável? ", n1.isprintable()) ##verifica se é printável
print("Ele contém um espaço em branco? ", n1.isspace()) ##verifica se é espaço em branco
print("Ele contém pelo menos um dígito?", n1.isdigit()) ##verifica se a variável contem digitos
print("Ele é um identificador válido? ", n1.isidentifier()) ##verifica se é uma string sem erros de sintaxe ou válida
print("Está capitalizada? ",n1.istitle())##verifica se a primeira letra de cada palavra está em maiúsculo e o resto minúculo.

#What's the primitive type of this value?
#Is it numeric?
#Is it a letter?
#Is it a letter and a number?
#Does it have only lowercase letters?
#Does it have only uppercase letters?
#Is it decimal?
#Is it printable?
#Does it have a white space?
#Does it have at least one digit?
#Is it a valid identifier?
#Is it capitalized?
