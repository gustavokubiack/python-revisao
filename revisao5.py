#Exercício 1
def converter_temperatura (f):
    c = (f - 32) * 5 / 9
    print("Temperatura em Celcius: {}".format(c))
f = float(input("Temperatura em Fahrenheit: "))
converter_temperatura(f)


#Exercício 2
import math

def pitagoras (a, b):
    hipotenusa = a ** 2 + b **2
    hipotenusa = math.sqrt(hipotenusa)
    print("Valor da Hipotenusa: {}".format(hipotenusa))

a = float(input("Valor A: "))
b = float(input("Valor B: "))
pitagoras(a, b)

#Exercício 3
def notas (nota1, nota2):
    media = (nota1 + nota2) / 2

    if nota1 > 10 or nota2 > 10:
        print("Erro, informe notas de 0 a 10.")
    elif media >= 6:
        print("PARABÉNS! Você foi aprovado.")
    else:
        print("Reprovado")

nota1 = float(input("Nota1: "))
nota2 = float(input("Nota2: "))
notas(nota1, nota2)

#Exercício 4
def pesoideal (h, sexo):
    
    if sexo == 1:
        mulher = (62.1 * h) - 44.7
        mulher = round(mulher,2)
        print("Peso ideal: {}kg".format(mulher))
    elif sexo == 2:
        homem = (72.7 * h) - 58
        homem = round(homem,2)
        print("Peso ideal: {}kg".format(homem))
    else:
        print("Erro! Informe 1 para mulher e 2 para homem.")

sexo = int(input("Sexo: 1 Fem / 2 Masc: "))
h = float(input("Altura: "))
pesoideal(h, sexo)

#Exercício 5
def poligonos (lado, medida):

    if lado == 3:
        perimetro_triangulo = medida * 3
        print("É um triângulo \nPerímetro: {}".format(perimetro_triangulo))
    elif lado == 4:
        area_quadrado = medida * 2
        print("É um quadrado \nÁrea: {}".format(area_quadrado))
    elif lado == 5:
        print("É um pentágono")
    else:
        print("Erro! Informe lados 3, 4 ou 5.")
        
lado = float(input("Lados do polígono: "))
medida = float(input("Medida de cada lado: "))
poligonos(lado, medida)

#Exercício 7
def num_mes (mes):
    if mes == 1:
            print("Janeiro")
    elif mes == 2:
            print("Fevereiro")
    elif mes == 3:
            print("Março")
    elif mes == 4:
            print("Abril")
    elif mes == 5:
            print("Maio")
    elif mes == 6:
            print("Junho")
    elif mes == 7:
            print("Julho")
    elif mes == 8:
            print("Agosto")
    elif mes == 9:
            print("Setembro")
    elif mes == 10:
            print("Outubro")
    elif mes == 11:
            print("Novembro")
    elif mes == 12:
            print("Dezembro")
    else:
        print("Erro! Informe números de 1 a 12.")

mes = int(input("Número: "))
num_mes(mes)    

#Exercício 8
def dia_semana(dia):
    if dia == 1:
        print("Domingo")
    elif dia == 2:
        print("Segunda")
    elif dia == 3:
        print("Terça")
    elif dia == 4: 
        print("Quarta")
    elif dia == 5:
        print("Quinta")
    elif dia == 6: 
        print("Sexta")
    elif dia == 7:
        print("Domingo")
    else:
        print("Erro! Informe números de 1 a 7.")

dia = int(input("Dia: "))
dia_semana(dia)

#Exercício 9
def divisivel (x, y):

    if y % x == 0:
        print("1")
    else:
        print("0")

x = int(input("Valor de x: "))
y = int(input("Valor de y: "))
divisivel(x, y)

#Exercício 10
def maior (a, b):
    if a > b:
        print("Maior valor = a")
    else:
        print("Maior valor = b")

a = int(input("Valor de a: "))
b = int(input("Valor de b: "))
maior(a, b) 

#Exercício 11
def pol_cm (pol, cm):
    cm = pol * 2.54
    print("Valor em centímetros: {}".format(cm))

pol = int(input("Valor em polegada: "))
pol_cm(pol, cm) 