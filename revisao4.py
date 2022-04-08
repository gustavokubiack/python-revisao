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
acima_media = 0
for item in range(10):
    notas.append(float(input("Nota: ")))
    soma = soma + notas[item]
    media = soma / 10
    if item >= 7:
        acima_media = acima_media + 1

for i in range(len(notas)):
    print("Nota {}. Média = {}. Notas acima da média: {} ".format(notas[i], media, acima_media))






#Exercício 6
num = list(range(200))
num = sum(num)
print(num)

#Exercício 7
numeros = list(range(200))
numeros.reverse()
print(numeros)

