# exercício 1
soma = 0
contapos = 0
for i in range(5):
    num = int(input("Informe um número: "))
    if num < 0:
        print("É negativo")
    else:
        soma = soma + num
        contapos = contapos +1 
        media = soma / contapos   
print("A soma dos números é: {}. A quantidade de positivos é {}. A média dos números é {}.".format(soma, contapos, media))
    
#exercício 2
par = 0
impar = 0
for i in range(5):
    num =int(input("Informe um valor: "))
    if num % 2 == 0:
        par = par + 1
    else:
        num % 2 == 1
        impar = impar + 1
print("A quantidade de par é: {}. A quantidade de ímpar é {}. ".format(par, impar))

#exercício 3
maior = 0
menor = 0
quant = 0
for i in range(5):
    num = int(input("Valor: "))
    quant = quant + 1
    if quant == 1:
        menor = maior = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
print("O maior valor é: {} e o menor valor é {}.".format(maior, menor))

#exercício 4
soma_par = 0
soma_impar = 0
for i in range(5):
    num = int(input("Informe um valor: "))
    if num % 2 == 0:
        soma_par = soma_par + num
    else:
        num % 2 == 1
        soma_impar = soma_impar + num
print("A soma dos números pares é: {}. \n A soma dos números ímpares é: {}.".format(soma_par, soma_impar))

#exercício 5
soma_altura = 0
quantidade_altura = 0 
for i in range(5):
    altura = float(input("Informe a altura: "))
    soma_altura = soma_altura + altura
    quantidade_altura = quantidade_altura + 1
    media = soma_altura / quantidade_altura
print("A média das alturas é {}." .format(media))

#exercício 6
negativo_num = 0
for i in range(5):
    num = int(input("Informe um valor: "))
    if num < 0:
        negativo_num = negativo_num +1
print("O quantidade de negativos é: {}.".format(negativo_num))

#exercício 7
tinta = 0
while tinta <= 100:
    print("A caneta está funcionando.")
    tinta = tinta + 2
    if tinta == 100:
        print("A caneta parou de funcionar.")


#Exercício 8
contagem_altura = 0
soma_alturas = 0
menor = maior = 0
quantidade = 0
while contagem_altura <= 5:
    inscr = int(input("Informe a inscrição do atleta: "))
    altura = int(input("Informe a altura do atleta: "))
    contagem_altura = contagem_altura + 1
    soma_alturas = soma_alturas + altura
    media = soma_alturas / contagem_altura
    quantidade = quantidade + 1
    if quantidade ==1:
        maior = menor = altura
    else:
        if altura > maior:
            maior = altura
        if altura < menor:
            menor = altura

print("A média é {}. Maior altura: {}. Menor altura: {}.".format(media, maior, menor))

#Exercício 9
x = 1.0
while x <= 5.0:
    y = (3 + (2 * x) + 6 * x ** 2) / (1 + (9 * x) + 16 * x ** 2)
    x = x + 0.1
    y = round(y,6)
    print("y = {}".format(y))

#Exercício 10
num = int(input("Fatorial de: "))
fat = 1
i = 2
while i <= num:
    fat = fat * i
    i = i + 1
print(fat) 

#Exercício 11
num = 1
while num <= 100:
    print(num)
    num = num + 1
    soma = num * 50
print("A soma da série de 1 a 100 é {}" .format(soma))

#Exercício 12
divisores = 1
cont_div = 1
num = int(input("Informe um valor: "))
while divisores <= num:
    if num % divisores == 0:
        print("{} é dividido por {}. Total de divisores: {}".format(num, divisores, cont_div))
        cont_div = cont_div +1
    divisores = divisores + 1

#Exercício 13
resp = "s"
soma = 0
cont_idade = 0
while resp == "s":
    idade = int(input("Idade: "))

    if idade == 0:
        print("Valor inválido")
    else:
        soma = soma + idade
        cont_idade = cont_idade + 1
        media = soma / cont_idade
    resp = str(input("Deseja digitar mais um valor? s (SIM) / n (NÃO) "))

print("A média de idades é: {}".format(media))


#Exercício 14

resp = "s"
soma_peixes = 0
limite_diario = int(input("Limite diário (kg): "))
while resp == "s":
    peso_peixe = int(input("Peso do peixe (g): "))
    peso_peixe = peso_peixe / 1000
    soma_peixes = soma_peixes + peso_peixe

    if peso_peixe > limite_diario:
        print("Peso do peixe superior ao limite diário")
    elif soma_peixes > limite_diario:
        print("Limite diário atingido")
    else:
        print("A soma atual dos peixes: {}g".format(soma_peixes))

    resp = str(input("Deseja digitar mais um valor? s (SIM) / n (NÃO) "))

print("Peso dos peixes: {}kg".format(soma_peixes))

#Exercício 15
nome = ""
while nome != "ULTIMO":
    nome = str(input("Nome: "))
    endereco = str(input("Endereço: "))
    valor_compra = int(input("Valor da compra: "))

    if valor_compra > 500:
        desconto = (valor_compra * 20) / 100
        valor_compra = valor_compra - desconto

    if valor_compra <= 500:
        desconto = (valor_compra * 15) / 100
        valor_compra = valor_compra - desconto
    print ("{}. Endereço: {}. Valor da compra com desconto: R${}".format(nome, endereco, valor_compra))

print("Fim do Programa")