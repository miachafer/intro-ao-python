# 1. Pergunte ao usuário em qual cidade e o estado em que ele(a) mora

# 2. Imprima uma mensagem diga a cidade em que o usuário mora. 
#    O nome da cidade deve estar todo em letras maiúsculas.

# 3. Imprima uma mensagem diga o estado em que o usuário mora. 
#    O nome do estado deve estar todo em letras maiúsculas.
#    Utilize uma forma de formatação de string diferente da que foi usada no item 2.

print('Em qual cidade você mora?')
cidade = input()

print('Em qual estado você mora?')
estado = input()

print('\nCidade: ' + cidade.lower())
print('Estado: ' + estado.upper())