import time

# Crie um decorator que calcule o tempo de execução de uma determinada função

def timeofexecution(func):
    def wrapper(x, y):
        tempo_inicial = time.time()
        func(x, y)
        tempo_execucao = time.time() - tempo_inicial
        print(f"Levou {tempo_execucao} segundo.")
    return wrapper

# Aplique seu decorator na função abaixo e veja quanto tempo a busca de um mesmo valor em um set e uma lista demoram para serem executadas

@timeofexecution
def encontrar_item(container, item):
    return item in container

def main():
    tamanho = 1000000
    set_grande = set(range(tamanho))
    lista_grande = list(range(tamanho))
    item = 500399
    encontrar_item(set_grande, item) # Output: Levou 0.0 segundo.
    encontrar_item(lista_grande, item) # Output: Levou 0.0015559196472167969 segundo.

if __name__ == '__main__':
    main()