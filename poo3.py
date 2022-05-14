#Exercício 1
class Usuario: 
    def __init__(self, nome):
        self.nome = nome

    def hello (self):
        return f"Olá, {self.nome}."

    def registrar (self):
        return ">> registrado"

    def mail (self):
        return ">> e-mail enviado"

        
user1 = Usuario ("Jane")
print(user1.hello(), user1.registrar(), user1.mail())

#Exercício 2
class Carro:
    
    def __init__(self, nomeCarro, nomeMotorista):
        self.nomeMotorista = nomeMotorista
        self.nomeCarro = nomeCarro

    def ligar (self):
        return f"{self.nomeCarro} foi ligado."

    def dirigir (self):
        return f"{self.nomeMotorista} está dirigindo o carro: {self.nomeCarro}."

    def frear (self):
        return f"{self.nomeCarro} freou."

    def desligar (self):
        return f"{self.nomeMotorista} desligou o carro."

car1 = Carro("Ferrari", "Jane")
print(car1.ligar())
print(car1.dirigir())
print(car1.frear())
print(car1.desligar())