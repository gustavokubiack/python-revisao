class Usuario:

    def __init__(self, primeiroNome, segundoNome):
        self.primeiroNome = primeiroNome
        self.segundoNome = segundoNome


    def getNomeCompleto(self):
        return f"Nome completo: {self.primeiroNome} {self.segundoNome}."

usuario1 = Usuario("Johnny", "Bravo")
print(usuario1.getNomeCompleto())