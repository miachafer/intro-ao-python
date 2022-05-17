# Crie uma lista com 60 números começando com o valor 1 e indo até o número 60 (ou seja, o número 60 deve estar na lista).

lista = [i for i in range(1, 61)]

print(lista)

# Imprima todos os itens da sua lista de índice par. Imprima o índice e o item.
print('índice | item')
print('------ | ----')
for i, item in enumerate(lista):
    if i%2 == 0:
        print(f'  {i}  | {item}')
