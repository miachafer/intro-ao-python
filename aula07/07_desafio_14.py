import sys
import requests
import json
import colorama

colorama.init()

# Crie uma aplicação que permita ao usuário obter informações sobre um determinado feitiço.
# O usuário deve digitar o nome de um feitiço como entrada para a nossa aplicação através da linha de comando. Por exemplo:
# python 07_desafio_14.py Vanishing Spell
# Você deverá obter os dados sobre o feitiço diretamente do JSON disponível em
# https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json
# Utilize a biblioteca requests para ler o JSON.
# Ao final do programa, imprima os dados sobre o feitiço que ele solicitou.
# Se o feitiço não foi encontrado, lance uma exceção.

# -------------------------------------------------

# Recebendo do usuário via linha de comando o nome do feitiço
# Exemplos de feitiços para teste:
# Vanishing Spell
# Unbreakable Vow
# Snake Summons Spell

entrada = sys.argv
feitico = ' '.join(entrada[1::])

# Função que realiza a requisição usando requests
def requisicao():
    URL = "https://construdelas.blob.core.windows.net/intro-ao-python/feiticos.json"
    # Fazendo a requisição
    response = requests.get(URL) # Response 200    
    # Colocando a response em formato de texto (json)
    response = response.json() # type: dict
    return response

# Função que retorna a descrição do feitiço inserido pelo usuário
def main():
    feiticos = requisicao()
    if feitico in feiticos:
            resposta = feiticos.get(feitico)
            print(
                "Feitiço: ", feitico, "\n"
                "Encantamento: ", resposta.get('encantamento'), "\n"
                "Tipo: ", resposta.get('tipo'), "\n"
                "Descrição: ", resposta.get('descricao'), "\n"
                "Cor da luz: ", resposta.get('cor_da_luz')
                )
    else:
        raise NameError(colorama.Fore.RED + "Feitiço inválido.")
        print(colorama.Style.RESET_ALL + "")

if __name__ == '__main__':
    main()
