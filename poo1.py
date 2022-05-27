#Exercício com 2 testes
class Usuario:

    def __init__(self, nome, sobrenome):
        self.nome =  nome
        self.sobrenome = sobrenome

    def hello (self):
        return "Olá,"


usuario1 =  Usuario(
    nome = str(input("Nome: ")),
    sobrenome = str(input("Sobrenome: ")),
)
print(usuario1.hello(), usuario1.nome, usuario1.sobrenome)

usuario2 = Usuario("Jane", "Silva")
print(usuario2.nome, usuario2.sobrenome)

#Exercício sem Input
class Usuario:

    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome 

    def hello (self):
        return ("Olá, {} {}".format(self.nome, self.sobrenome))

usuario1 = Usuario("Gustavo", "Kubiack")
print(usuario1.hello())

usuario2 = Usuario("Jane", "Silva")
print(usuario2.hello())