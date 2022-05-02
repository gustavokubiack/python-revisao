#Escreva a classe Usuario e adicione as propriedades e o método (em Python). Crie a primeira instância e chame-a de usuario1. Defina os valores do primeiro e último nome para usuario1. Obter o nome e sobrenome do usuário e imprima-os na tela com o comando print. Use o método que retorna “Olá” com as variáveis primeiro nome e último nome para dizer Olá ao usuário. Crie (instancie) outro objeto. Chame-o de usuario2, dê a ele o primeiro nome de “Jane” e o sobrenome de “Silva”, e depois diga “Olá” ao usuário.

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
