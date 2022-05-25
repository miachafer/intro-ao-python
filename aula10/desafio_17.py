# O banco Banco Delas é um banco moderno e eficiente, com vantagens exclusivas para clientes mulheres.
# Modele um sistema orientado a objetos para representar contas correntes em do Banco Delas seguindo os requisitos abaixo.

# 1. Cada conta corrente pode ter um ou mais clientes como titular.
# 2. O banco controla apenas o nome, o telefone e a renda mensal de cada cliente.
# 3. A conta corrente apresenta um saldo e uma lista de operações de saques e depósitos.
#   Quando a cliente fizer um saque, diminuiremos o saldo da conta corrente
#   Quando ela fizer um depósito, aumentaremos o saldo.
# 4. Clientes mulheres possuem em suas contas um cheque especial de valor igual à sua renda mensal, ou seja, elas podem sacar valores que deixam a sua conta com valor negativo até -renda_mensal.
# 5. Clientes homens por enquanto não têm direito a cheque especial.

# Para modelar seu sistema, utilize obrigatoriamente os conceitos "classe", "herança" e "polimorfismo".
# Opcionalmente, você pode também utilizar "propriedades", "encapsulamento" e "classe abstrata".

from abc import ABC, abstractmethod
from datetime import datetime 

class Pessoa(ABC):
    def __init__(self, nome):
        self.nome = nome
        self.telefone = 0
        self.renda_mensal = 0.0

    def __str__(self) -> str:
        pass

    @abstractmethod
    def set_telefone(self, telefone):
        pass

    @abstractmethod
    def set_renda_mensal(self, renda_mensal):
        pass
    
    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def get_telefone(self):
        pass

    @abstractmethod
    def get_renda_mensal(self):
        pass


class Cliente(Pessoa):

    def __init__(self, nome):
        super().__init__(nome) 
        self.genero = None

    def __str__(self) -> str:
        return f'Nome: {self.nome}, Telefone: {self.telefone}, Renda: {self.renda_mensal}, Mulher: {self.genero}'

    def get_nome(self):
        return self.nome

    def set_genero(self, genero): # Mulher: True
        self.genero = genero

    def get_genero(self):
        return self.genero

    def set_telefone(self, telefone):
        self.telefone = telefone

    def get_telefone(self):
        return self.telefone

    def set_renda_mensal(self, renda_mensal):
        self.renda_mensal = renda_mensal

    def get_renda_mensal(self):
        return self.renda_mensal

class Conta:
    def __init__(self, id, Cliente):
        self.id = id
        self.titular = Cliente.__str__()
        self.saldo = 0.0
        self.extrato = []

    def __str__(self):
        return f"Conta {self.id}\nTitular: {self.titular}\nSaldo: {self.saldo}\nExtrato: {self.extrato}"

    def set_titular(self, Cliente):
        if type(self.titular) != list:
            primeiro_titular = self.titular
            segundo_titular = Cliente.__str__()
            self.titular = []
            self.titular.append(primeiro_titular)
            self.titular.append(segundo_titular)
        else:
            outro_titular = Cliente.__str__()
            self.titular.append(outro_titular)

    def get_titular(self):
        return self.titular

    def get_saldo(self):
        return self.saldo

    def get_extrato(self):
        return self.extrato

    def depositar(self, valor):
        self.saldo += valor
        operacao = {'Operação': {'Tipo': 'Depósito', 'Valor': valor, 'Status': 'Sucesso', 'Data': datetime.now().strftime("%d/%m/%Y %H:%M:%S")}}
        self.extrato.append(operacao)

    def saque(self, valor):
        if (self.saldo - valor) > 0:
            self.saldo -= valor
            operacao = {'Operação': {'Tipo': 'Saque', 'Valor': valor, 'Status': 'Sucesso', 'Data': datetime.now().strftime("%d/%m/%Y %H:%M:%S")}}
            self.extrato.append(operacao)
        else:
            self.saldo = self.saldo
            print("Saldo insuficiente.\n")
            operacao = {'Operação': {'Tipo': 'Saque', 'Valor': valor, 'Status': 'Falha', 'Data': datetime.now().strftime("%d/%m/%Y %H:%M:%S")}}
            self.extrato.append(operacao)

    # def cheque_especial():
    #     if type(self.titular) is Cliente:
    #         if Cliente.get_genero(self) == True:
    #             cheque_especial = True
    #             return(cheque_especial)
    #     if type(self.titular) == list:
    #         self_titular = titulares
    #         for titular in titulares:
    #             if titular.get_genero == True:
    #                 cheque_especial = True
    #                 return(cheque_especial)
    #                 break
    #     else:
    #         cheque_especial == False