#Exercício 1
lista = list(range(100))
print(lista)

#Exercício 2
notas = []
soma = 0
for i in range(10):
    notas.append(float(input("Nota: ")))
    soma = soma + notas[i]
media = soma / 10

for i in range(len(notas)):
    print("Nota {}. Média = {}".format(notas[i], media))

#Exercício 3
notas = []
soma = 0

for item in range(10):
    notas.append(float(input("Nota: ")))
    soma = soma + notas[item]
    media = soma / 10

acima_media = 0
for item in range(10):
    if notas[item] >= media:
        acima_media = acima_media + 1

for i in range(len(notas)):
    print("Nota {}. Média = {}. Notas acima da média: {} ".format(notas[i], media, acima_media))

#Exercício 4
notas = []
soma = 0

for item in range(10):
    notas.append(float(input("Nota: ")))
    soma = soma + notas[item]
    media = soma / 10

maior = notas[0]
menor = notas[0]
for i in notas:
    if i > maior:
        maior = i
    elif i < menor:
        menor = i

abaixo_media = 0
for item in range(10):
    if notas[item] <= media:
        abaixo_media = abaixo_media + 1

for i in range(len(notas)):
    print("Nota {}. Média = {}. Notas acima da média: {} Maior nota: {} Menor nota: {}".format(notas[i], media, abaixo_media, maior, menor))


#Exercício 6
num = list(range(200))
num = sum(num)
print(num)

#Exercício 7
numeros = list(range(200))
numeros.reverse()
print(numeros)

#Exercício 8
lista1 = []
lista2 = []
lista3 = []

for i in range(10):
    lista1.append(int(input("Números lista1: ")))
    lista2.append(int(input("Números lista2: ")))

    num = lista1[i] + lista2[i]
    lista3.append(num)
print("Lista1: {} \nLista2: {} \nLista3: {}".format(lista1,lista2, lista3))

#Exercício 9
lista1 = []
lista2 = []

for i in range(5):
    lista1.append(float(input("Nota1: ")))
    lista2.append(float(input("Nota2: ")))
    lista3 = list(lista1 + lista2)
    lista3[::2] = lista1
    lista3 [1 :: 2] = lista2
print(lista3)

#Exercício 11
lista1 = []
lista2 = []

for item in range(10):
    lista1.append(float(input("Número: ")))
    
for num in lista1:
    if num % 2 == 0:
        num = num * 3
        lista2.append(num)
    elif num % 2 == 1:
        num = num / 2
        lista2.append(num)
print("Lista 1: {} \nLista 2: {}".format(lista1, lista2))

#Exercício 15
lista1 = []
for item in range(20):
    lista1.append(int(input("Número: ")))
    lista1.sort()
print(lista1)

