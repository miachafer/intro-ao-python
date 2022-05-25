from desafio_17 import *

print("-------------CLIENTES-------------\n")
homem = Cliente("Abraão")
homem.set_telefone(123456789)
homem.set_renda_mensal(5000.00)
homem.set_genero(False)
print(homem)

print()
mulher = Cliente("Sara")
mulher.set_telefone(987654321)
mulher.set_renda_mensal(7000)
mulher.set_genero(True)
print(mulher)

print()
print("--------------CONTAS--------------\n")

conta0 = Conta(0, homem)
print(conta0)

print("\nDepósito de 2000.00\n")
conta0.depositar(2000)
print(conta0)

print("\nSaque de 800.00\n")
conta0.saque(800)
print(conta0)

# print("\nAdicionando mais de um titular à conta\n")
# conta0.set_titular(mulher)
# print(conta0)
