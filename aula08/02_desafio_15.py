# Crie uma classe que modele o objeto "carro".
# Um carro tem os seguintes atributos: ligado, cor, modelo, velocidade.
# Um carro tem os seguintes comportamentos: liga, desliga, acelera, desacelera.

class Carro:
    def __init__(self):
        self.ligado = False
        self.cor = None
        self.modelo = None
        self.velocidade = 0

    def __str__(self) -> str:
        return f'Carro \nLigado: {self.ligado} \nCor: {self.cor} \nModelo {self.modelo} \nVelocidade atual: {self.velocidade}'
    
    def liga(self):
        if self.ligado == False:
            self.ligado = True
        else:
            print("O carro já está ligado.")

    def desliga(self):
        if self.ligado == True:
            self.ligado = False
            self.velocidade = 0
        else:
            print("O carro já está desligado.")

    def acelera(self):
        if self.velocidade <= 190:
            self.velocidade += 10
        else:
            print("Velocidade máxima atingida.")

    def desacelera(self):
        if self.velocidade >= 10:
            self.velocidade -= 10
        else:
            self.velocidade = self.velocidade

# Crie uma instância da classe carro.

carro1 = Carro()

# Faça o carro "andar" utilizando os métodos da sua classe.

carro1.liga()
carro1.acelera()
carro1.acelera()
carro1.acelera()
carro1.acelera()
carro1.acelera()
print(carro1)
print("---------------------------")

# Faça o carro "parar" utilizando os métodos da sua classe.

carro1.desliga()
print(carro1)