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
    # Cliente tem 1 atributo (gênero) além dos atributos de Pessoa
    def __init__(self, nome):
        super().__init__(nome) 
        self.genero = None

    def __str__(self) -> str:
        return f'Nome: {self.get_nome}; Telefone: {self.get_telefone}; Renda: {self.get_renda_mensal}; Mulher: {self.get_genero}'

    @property
    def get_nome(self):
        return self.nome

    def set_genero(self, genero): # Mulher: True
        self.genero = genero

    @property
    def get_genero(self):
        return self.genero

    def set_telefone(self, telefone):
        self.telefone = telefone

    @property
    def get_telefone(self):
        return self.telefone

    def set_renda_mensal(self, renda_mensal):
        self.renda_mensal = renda_mensal

    @property
    def get_renda_mensal(self):
        return self.renda_mensal


class Conta:
    def __init__(self, id, Cliente):
        self.id = id
        self.titular = Cliente.__str__()
        self.saldo = 0.0
        self.extrato = []
        self.cheque_especial = Cliente.get_genero
        self.renda = Cliente.get_renda_mensal

    def __str__(self):
        return f"Conta {self.id}; Titular: {self.titular}; Saldo: {self.saldo}"

    # Função válida para adicionar mais de um titular à conta
    def set_titular(self, Cliente):
        # Se só houver um titular na conta:
        if type(self.titular) != list:
            primeiro_titular = self.titular
            segundo_titular = Cliente.__str__()
            self.titular = []
            self.titular.append(primeiro_titular)
            self.titular.append(segundo_titular)
        # Se a conta já tiver uma lista de titulares
        else:
            outro_titular = Cliente.__str__()
            self.titular.append(outro_titular)

    @property
    def get_titular(self):
        return self.titular

    @property
    def get_saldo(self):
        return self.saldo

    @property
    def get_extrato(self):
        return self.extrato

    @property
    def get_cheque_especial(self):
        # Conta com única titular
        if type(self.titular) != list:
            return self.cheque_especial
        # Conta conjunta
        else:
            self.cheque_especial = False
            return self.cheque_especial
    
    @property
    def get_renda(self):
        return self.renda

    # Essa função imprime os dados de transação
    # Seria bom esse método ficar privado
    def dados_transacao(self, tipo, status, montante):
        transacao = {'Operação': {'Tipo': tipo, 'Valor': montante, 'Status': status, 'Data': datetime.now().strftime("%d/%m/%Y %H:%M:%S")}}
        return transacao

    def depositar(self, valor):
        self.saldo += valor
        operacao = self.dados_transacao("Depósito", "Sucesso", valor)
        self.extrato.append(operacao)   

    def saque(self, valor):
        if (self.saldo - valor) > 0:
            self.saldo -= valor
            operacao = self.dados_transacao("Saque", "Sucesso", valor)
            self.extrato.append(operacao)
        else:
            # Regra de cheque especial para conta com único titular
            if type(self.titular) != list: 
                cheque_especial = self.get_cheque_especial
                # Cliente mulher: tem direito a cheque especial
                if cheque_especial: 
                    valor_cheque_especial = self.renda * (-1)
                    # Cliente ainda não estourou o cheque especial e pode usá-lo
                    if (self.saldo - valor) > valor_cheque_especial:
                        self.saldo -= valor
                        operacao = self.dados_transacao("Saque", "Sucesso", valor)
                        self.extrato.append(operacao)     
                    # Cliente estourou o cheque especial 
                    else: 
                        self.saldo = self.saldo
                        print("Saldo insuficiente.")
                        operacao = self.dados_transacao("Saque", "Falha", valor)
                        self.extrato.append(operacao)        
                # Cliente homem: não tem direito a cheque especial
                else:
                    self.saldo = self.saldo
                    print("Saldo insuficiente.")
                    operacao = self.dados_transacao("Saque", "Falha", valor)
                    self.extrato.append(operacao)
            # Conta conjunta: não tem direito a cheque especial
            else:
                self.saldo = self.saldo
                print("Saldo insuficiente.")
                operacao = self.dados_transacao("Saque", "Falha", valor)
                self.extrato.append(operacao)


