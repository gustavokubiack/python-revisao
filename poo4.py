#Exercicio 2
class Usuario:
    
    __primeiroNome = ""

    def setUser(self, primeiroNome):
        self.__primeiroNome = primeiroNome

    def getUser(self):
        return f"O nome do usuário é: {self.__primeiroNome}"

usuario1 = Usuario()
usuario1.setUser("Joe")
print(usuario1.getUser())

#Exercicio 3

class Empregado:

    def __init__(self, nome, projeto):

        self.nome = nome
        __salario = ""
        self.projeto = projeto

    def trabalho (self):
        return f"Nome do funcionário: {self.nome} \nNome do projeto: {self.projeto}"

    def setSalario(self, salario):
        self.__salario = salario
    
    def mostrar (self):
        return f"Nome do funcionário: {self.nome} \nSalário: {self.__salario}"

func1 = Empregado("Gustavo", "Projeto Social")
print(func1.trabalho())

func1.setSalario(10.00)
print(func1.mostrar())

#Exercício 4

class Robo():
    __nome = ""
    __ano_construcao = ""

    def diga_alo(self):
        return f"Nome do robô: {self.__nome} \nAno de constução: {self.__ano_construcao}"
    
    def setNome(self, nome):
        self.__nome = nome
    
    def setAnoConstrucao(self, ano_construcao):
        self.__ano_construcao = ano_construcao
    
robo1 = Robo()
robo1.setNome("Bob")
robo1.setAnoConstrucao("2022")
print(robo1.diga_alo())

#Exercício 5
class Laptop:

    __preco = ""

    def get_preco(self):
        return f"Preço do laptop: {self.__preco}"
    
    def set_preco(self, preco):
        self.__preco = preco

laptop1 = Laptop()
laptop1.set_preco(3999)
print(laptop1.get_preco())   

#Exercício 6
class Pessoa:

    __primeiroNome = ""
    __ultimoNome = ""

    def getPrimeiroNome(self):
        return f"Nome: {self.__primeiroNome}"
    
    def getUltimoNome(self):
        return f"Sobrenome: {self.__ultimoNome}"

    def setPrimeiroNome(self,nome):
        self.__primeiroNome = nome

    def setUltimoNome(self, sobrenome):
        self.__ultimoNome = sobrenome

pessoa1 = Pessoa()
pessoa1.setPrimeiroNome("João")
pessoa1.setUltimoNome("Carvalho")
print(pessoa1.getPrimeiroNome())
print(pessoa1.getUltimoNome())