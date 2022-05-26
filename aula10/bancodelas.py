from desafio_17 import *

# TESTES
# OK Criação de clientes: homens e mulheres
# OK Criação de contas:
    # OK Conta de mulher
    # OK Conta de homem
    # OK Conta conjunta - adição de titular
# OK Depósito
# OK Saque
    # OK Comum
    # OK Cheque especial para mulher
    # OK Cheque especial bloqueado para mulher que já usou o cheque especial
    # OK Cheque especial bloqueado para homem
    # OK Cheque especial bloqueado para conta conjunta

print()
print("-------------CLIENTES-------------\n")
homem1 = Cliente("Abraão")
homem1.set_telefone(123456789)
homem1.set_renda_mensal(3000.00)
homem1.set_genero(False)
print(homem1)

mulher1 = Cliente("Sara")
mulher1.set_telefone(987654321)
mulher1.set_renda_mensal(1000.00)
mulher1.set_genero(True)
print(mulher1)

homem2 = Cliente("Isaque")
homem2.set_telefone(369852147)
homem2.set_renda_mensal(2500.00)
homem2.set_genero(False)
print(homem2)

mulher2 = Cliente("Rebeca")
mulher2.set_telefone(147852369)
mulher2.set_renda_mensal(2000.00)
mulher2.set_genero(True)
print(mulher2)

print()
print("--------------CONTAS--------------\n")

conta0 = Conta(0, homem1)
print("CONTA COM TITULAR HOMEM:")
print(conta0)
print("CHEQUE ESPECIAL PARA CONTA DE HOMEM:")
print(conta0.get_cheque_especial)
print()

conta1 = Conta(1, mulher1)
print("CONTA COM TITULAR MULHER:")
print(conta1)
print("CHEQUE ESPECIAL PARA CONTA DE MULHER:")
print(conta1.get_cheque_especial)
print()

conta2 = Conta(2, mulher2)
conta2.set_titular(homem2)
print("CONTA COM DOIS TITULARES:")
print(conta2)
print("TITULARES DA CONTA 2:")
print(conta2.get_titular)
print("CHEQUE ESPECIAL PARA CONTA CONJUNTA:")
print(conta2.get_cheque_especial)

print()
print("------------OPERAÇÕES------------\n")

print("DEPÓSITOS\n")

print("SALDO DA CONTA 0:", conta0.get_saldo)
print("DEPÓSITO DE 300 EM CONTA DE HOMEM - CONTA 0")
conta0.depositar(300)
print("SALDO DA CONTA 0:", conta0.get_saldo)

print()

print("SALDO DA CONTA 1:", conta1.get_saldo)
print("DEPÓSITO DE 500 EM CONTA DE MULHER - CONTA 1")
conta1.depositar(500)
print("SALDO DA CONTA 1:", conta1.get_saldo)

print()

print("SALDO DA CONTA 2:", conta2.get_saldo)
print("DEPÓSITO DE 700 EM CONTA CONJUNTA - CONTA 2")
conta2.depositar(700)
print("SALDO DA CONTA 2:", conta2.get_saldo)

print("\nSAQUES\n")

print("SALDO DA CONTA 0:", conta0.get_saldo)
print("SAQUE DE 125 EM CONTA DE HOMEM - CONTA 0")
conta0.saque(125)
print("SALDO DA CONTA 0:", conta0.get_saldo)

print()

print("SALDO DA CONTA 1:", conta1.get_saldo)
print("SAQUE DE 200 EM CONTA DE MULHER - CONTA 1")
conta1.saque(200)
print("SALDO DA CONTA 1:", conta1.get_saldo)

print()

print("SALDO DA CONTA 2:", conta2.get_saldo)
print("DEPÓSITO DE 650 EM CONTA CONJUNTA - CONTA 2")
conta2.saque(650)
print("SALDO DA CONTA 2:", conta2.get_saldo)

print("\nCHEQUE ESPECIAL\n")

print("SALDO DA CONTA 0:", conta0.get_saldo)
print("SAQUE DE 200 NA CONTA 0")
conta0.saque(200)
print("SALDO DA CONTA 0:", conta0.get_saldo)
print()

print("SALDO DA CONTA 1:", conta1.get_saldo)
print("SAQUE DE 350 NA CONTA 1")
conta1.saque(350)
print("SALDO DA CONTA 1:", conta1.get_saldo)
print("VALOR DISPONÍVEL DO CHEQUE ESPECIAL:", conta1.get_renda)
print("ESTOURANDO O CHEQUE ESPECIAL")
print("SAQUE DE 960 NA CONTA 1")
conta1.saque(960)
print("SALDO DA CONTA 1:", conta1.get_saldo)
print()

print("SALDO DA CONTA 2:", conta2.get_saldo)
print("SAQUE DE 200 NA CONTA 2")
conta2.saque(200)
print("SALDO DA CONTA 2:", conta2.get_saldo)
print()

############ OUTPUT ############
"""
-------------CLIENTES-------------

Nome: Abraão; Telefone: 123456789; Renda: 3000.0; Mulher: False
Nome: Sara; Telefone: 987654321; Renda: 1000.0; Mulher: True
Nome: Isaque; Telefone: 369852147; Renda: 2500.0; Mulher: False
Nome: Rebeca; Telefone: 147852369; Renda: 2000.0; Mulher: True

--------------CONTAS--------------

CONTA COM TITULAR HOMEM:
Conta 0; Titular: Nome: Abraão; Telefone: 123456789; Renda: 3000.0; Mulher: False; Saldo: 0.0
CHEQUE ESPECIAL PARA CONTA DE HOMEM:
False

CONTA COM TITULAR MULHER:
Conta 1; Titular: Nome: Sara; Telefone: 987654321; Renda: 1000.0; Mulher: True; Saldo: 0.0
CHEQUE ESPECIAL PARA CONTA DE MULHER:
True

CONTA COM DOIS TITULARES:
Conta 2; Titular: ['Nome: Rebeca; Telefone: 147852369; Renda: 2000.0; Mulher: True', 'Nome: Isaque; Telefone: 369852147; Renda: 2500.0; Mulher: False']; Saldo: 0.0
TITULARES DA CONTA 2:
['Nome: Rebeca; Telefone: 147852369; Renda: 2000.0; Mulher: True', 'Nome: Isaque; Telefone: 369852147; Renda: 2500.0; Mulher: False']
CHEQUE ESPECIAL PARA CONTA CONJUNTA:
False

------------OPERAÇÕES------------

DEPÓSITOS

SALDO DA CONTA 0: 0.0
DEPÓSITO DE 300 EM CONTA DE HOMEM - CONTA 0
SALDO DA CONTA 0: 300.0

SALDO DA CONTA 1: 0.0
DEPÓSITO DE 500 EM CONTA DE MULHER - CONTA 1
SALDO DA CONTA 1: 500.0

SALDO DA CONTA 2: 0.0
DEPÓSITO DE 700 EM CONTA CONJUNTA - CONTA 2
SALDO DA CONTA 2: 700.0

SAQUES

SALDO DA CONTA 0: 300.0
SAQUE DE 125 EM CONTA DE HOMEM - CONTA 0
SALDO DA CONTA 0: 175.0

SALDO DA CONTA 1: 500.0
SAQUE DE 200 EM CONTA DE MULHER - CONTA 1
SALDO DA CONTA 1: 300.0

SALDO DA CONTA 2: 700.0
DEPÓSITO DE 650 EM CONTA CONJUNTA - CONTA 2
SALDO DA CONTA 2: 50.0

CHEQUE ESPECIAL

SALDO DA CONTA 0: 175.0
SAQUE DE 200 NA CONTA 0
Saldo insuficiente.
SALDO DA CONTA 0: 175.0

SALDO DA CONTA 1: 300.0
SAQUE DE 350 NA CONTA 1
SALDO DA CONTA 1: -50.0
VALOR DISPONÍVEL DO CHEQUE ESPECIAL: 1000.0
ESTOURANDO O CHEQUE ESPECIAL
SAQUE DE 960 NA CONTA 1
Saldo insuficiente.
SALDO DA CONTA 1: -50.0

SALDO DA CONTA 2: 50.0
SAQUE DE 200 NA CONTA 2
Saldo insuficiente.
SALDO DA CONTA 2: 50.0
"""