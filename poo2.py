class Usuario:

    def __init__(self, primeiroNome, segundoNome):
        self.primeiroNome = primeiroNome
        self.segundoNome = segundoNome

    def hello (self):
        return ("Olá, {} {}".format(self.primeiroNome, self.segundoNome))

user1 = Usuario("Jonnie", "Bravo")
print(user1.hello())