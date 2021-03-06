#Exercício 1

class Bola:

    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor (self, novaCor):
        self.cor = novaCor

    def mostraCor(self):
        return f"A cor é {self.cor}"


bola1 = Bola("Vermelha", 10, "plástico")
bola1.trocaCor("Verde")
print(bola1.mostraCor())

#Exercício 2

class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def mudaValor(self, novoLado):
        self.lado = novoLado
        return f"Novo lado: {self.lado}"
    
    def retornaValor(self):
        return f"Lado do Quadrado: {self.lado}"
    
    def calculaArea (self):
        return f"Área do Quadrado: {self.lado * 2}"

quad1 = Quadrado(4)
quad1.mudaValor(5)
print(quad1.retornaValor())
print(quad1.calculaArea())

#Exercício 3

class Retangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def mudaLados(self, novaBase, novaAltura):
        self.base = novaBase
        self.altura = novaAltura
        return f"Nova base: {self.base} \nNova altura: {self.altura}"

    def retornaLados(self):
        return f"Base: {self.base} \nAltura: {self.altura}"

    def areaRet(self):
        return f"Área do retângulo: {(self.base * self.altura) / 2}"
    
    def perimetroRet(self):
        return f"Perímetro: {(self.base * 2)+(self.altura * 2)}"

#Teste sem input
ret1 = Retangulo(2,4)
print(ret1.areaRet())
print(ret1.perimetroRet())

#Teste com com input (pedindo a base e a altura)
ret2 = Retangulo(
    base = int(input("Informe o comprimento do local: ")),
    altura = int(input("Informe a largura do local: "))
)
print(ret2.areaRet())
print(ret2.perimetroRet())

#Exercício 4

class Funcionario:

    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def dadosFuncionario(self):
        return f"Nome do funcionário: {self.nome} \nSalário: {self.salario}"

    def novoSalario (self, porcentagem):
        porcentagemSalario = (porcentagem * self.salario) / 100
        self.salario = self.salario + porcentagemSalario
        return f"Novo salário: R${self.salario}"

func1 = Funcionario("Harry", 1000)
print(func1.novoSalario(10))
print(func1.dadosFuncionario())

#Exercício 5

class Carro:

    def __init__(self, consumo, combustivelTanque = 0):
        self.consumo = consumo
        self.combustivelTanque = combustivelTanque

    def obterGasolina(self):
        return f"Quantidade de gasolina no tanque: {self.combustivelTanque}L"

    def adicionarGasolina(self, gasolina):
        self.combustivelTanque = gasolina + self.combustivelTanque

    def andar(self, distancia):
        self.combustivelTanque = self.combustivelTanque - (distancia * self.combustivelTanque) / (self.combustivelTanque * self.consumo)
    

fusca = Carro(10,0)
fusca.adicionarGasolina(10)
print(fusca.obterGasolina())
fusca.andar(50)
print(fusca.obterGasolina())

#Exercício 6

class ContaCorrente:

    def __init__(self, numConta, nomeUsuario, saldo = 0):
        self.numConta = numConta
        self.nomeUsuario = nomeUsuario
        self.saldo = saldo

    def alteraNome(self, novoNome):
        self.nome = novoNome
        return f"Nome: {self.nome}"

    def deposito(self, deposito):
        self.saldo = self.saldo + deposito
        return f"Saldo da conta: R${self.saldo}"

    def saque(self, saque):
        self.saldo = self.saldo - saque
        return f"Saldo da conta: R${self.saldo}"

user1 = ContaCorrente(123, "Gustavo Kubiack")
print(user1.alteraNome("Gustavo Henrique Kubiack"))
print(user1.deposito(100))
print(user1.saque(25))



