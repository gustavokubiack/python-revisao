#Existe um erro, pois não tem como acessar uma propriedade privada, entretanto alterando o código é possível fazer o código rodar com sucesso mudando de uma propriedade privada para uma propriedade protegida.

class Usuario:
    _nomeUsuario = ""

    def setter(self, nome):
        self._nomeUsuario = nome
    
    def getter(self):
        return f"Olá, meu nome é {self._nomeUsuario} e estou acessando esse método pela classe filha."

class Admin(Usuario):

    def escrevaNome(self):
        return "Admin"

    def digaOla(self):
        return f"Olá Admin, {self._nomeUsuario}."

admin1 = Admin()
admin1.setter("Alan Turing")
admin1.getter()
print(admin1.getter())
print(admin1.digaOla())
