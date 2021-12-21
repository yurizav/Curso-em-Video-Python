print('\nIdentificador de Tipo Primitivo - Desafio 004\n')
var = input(('Digite qualquer coisa... \n'))

if var.isalpha():
    print(var, " é do tipo caractere!\n")
    if var.isupper():
        print(var, " está em caixa alta!\n")
    if var.islower():
        print(var, ' está em caixa baixa!\n')
        

if var.isnumeric():
    var = int(var)
    print(var," é um número!")
    if (var%2) == 0:
        print(var, ' é par!\n')
    else:
        print(var, ' é impar!\n')

if var.isspace():
    print('Por favor, digite algo!')
    



