# Você é a professora de Ciências e está lançando as notas das alunas.
# Você quer criar um sistema no qual suas alunas podem ver suas notas digitando o nome.
# As listas de alunas e notas se encontra abaixo. As notas podem variar de 0 a 100.
# Nessas listas, as notas estão na mesma ordem dos nomes, ou seja, a aluna no índice 4 tirou a nota no índice 4.

# Comece o programa perguntando o nome da aluna.
# Procure o nome digitado na lista de nomes e imprima uma mensagem com a nota que ela tirou.
# Notas abaixo de 60 devem ser impressas com a cor vermelha, e notas a partir de 90 devem ser impressas com a cor verde.
# Se o nome digitado não existir na lista, imprima uma mensagem de erro usando a cor vermelha.

import colorama
colorama.init()

alunas = ['Adriana', 'Bárbara', 'Franciele', 'Laís', 'Maria', 'Nayara', 'Patrícia', 'Renata', 'Sarah', 'Thainá']
notas = [78, 57, 80, 98, 54, 89, 90, 100, 71, 85]

def ver_nota():
    print('Digite o nome da aluna para ver sua nota:')
    nome_da_aluna = input()

    if nome_da_aluna not in alunas:
        print(colorama.Fore.RED + "Digite um nome válido")
        print(colorama.Style.RESET_ALL + "")
        ver_nota()

    for i, item in enumerate(alunas):
        if nome_da_aluna == item:
            if notas[i] < 60:
                print(f'A nota de {nome_da_aluna} é' + colorama.Fore.RED + f' {notas[i]}')
                print(colorama.Style.RESET_ALL + "")
            elif notas[i] > 90:
                print(f'A nota de {nome_da_aluna} é' + colorama.Fore.GREEN + f' {notas[i]}')
                print(colorama.Style.RESET_ALL + "")
            elif 90 > notas[i] > 60:
                print(f'A nota de {nome_da_aluna} é {notas[i]}')
                print(colorama.Style.RESET_ALL + "")

ver_nota()
