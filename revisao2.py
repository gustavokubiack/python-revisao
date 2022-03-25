#Ler um valor e escrever se é positivo, negativo ou zero.

num = int(input("Informe um valor: "))
if num == 0:
    print("O valor é igual a 0")
if num < 0:
    print("O valor é negativo")
if num > 0:
    print("O valor é positivo") 

#Ler um valor e escrever a mensagem É MAIOR QUE 10 se o valor lido for maior que 10, caso contrário escrever NÃO É MAIOR QUE 10.
num10 = int(input("Informe um valor: "))

if num10 >  10:
    print("O valor é maior que 10")
else:
    print("O valor é menor que 10")

#Calcule a soma de dois números, se o resultado for maior que 10, mostre-o na tela.

num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))
soma = num1 + num2 
if soma > 10:
    print("O resultado é {}".format(soma))
else:
    print("O valor é menor que 10")

#Entrar com um número e informar se ele é divisível por 5.

num1 = int(input("Informe um valor: "))
if num1 % 5 == 0:
    print("{} é divisível por 5".format(num1))
else:
    print("{} não é divísivel por 5".format(num1))

#Construir um algoritmo que indique se o número digitado está entre 20 e 90 ou não.

num1 = int(input("Informe um valor: "))
if num1 > 20 and num < 90:
    print("{} está entre 20 e 90".format(num1))
else:
    print("{} não está entre 20 e 90".format(num1))

#Ler o ano atual e o ano de nascimento de uma pessoa. Escrever uma mensagem que diga se ela poderá ou não votar este ano (não é necessário considerar o mês em que a pessoa nasceu).

ano_atual = int(input("Informe o ano atual: "))
data_nasc = int(input("Informe o ano em que nasceu: "))
diferenca = ano_atual - data_nasc
if diferenca >= 16:
    print("A pessoa pode votar")
else:
    print("A pessoa não pode votar")

#Entrar com o ano de nascimento de uma pessoa e imprimir a idade dela. Verificar se o ano digitado é válido.

data_nasc = int(input("Informe o ano que nasceu: "))
idade =  2022 - data_nasc
if data_nasc < 1 or data_nasc > 2022:
    print("Ano inválido")
else:
    print("Você tem {} anos" .format(idade))

#Entrar com a idade de uma pessoa e exibir a mensagem; Maior de idade, menor de idade ou acima de 65 anos.

idade = int(input("Informe sua idade: "))
if idade < 18:
    print("Você é menor de idade")
if idade >= 18 and idade < 65:
    print("Vocẽ é maior de idade")
else:
    print("Você é idoso")

#Ler as notas da 1a e 2a avaliações de um aluno. Calcular a média aritmética simples e escrever uma mensagem que diga se o aluno foi ou não aprovado (considerar que se a nota for igual ou maior que 6 o aluno é aprovado). Escrever também a média calculada.

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 6:
    print("Você foi aprovado")
else:
    print("Você foi reprovado")

#Escrever um algoritmo para ler duas notas de um aluno e escrever na tela a palavra “Aprovado” se a média das duas notas for maior ou igual a 7,0. Caso a média seja inferior a 7,0, o programa deve ler a nota do exame e calcular a média final. Se esta média for maior ou igual a 5,0, o programa deve escrever “Aprovado”, caso contrário deve escrever “Reprovado”.

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
media = (nota1 + nota2) / 2
if media >= 7:
    print("Você foi aprovado")
if media <= 7:
    print("Você foi reprovado, faça o exame!")
nota3 = float(input("Informe a nota do exame: "))
media_nova =(nota1 + nota2 + nota3) / 3
if media_nova > 5:
    print("Aprovado")
else:
    print("Reprovado")

#Escrever um algoritmo para ler a quantidade de horas aula dadas por dois professores e o valor por hora recebido por cada um. Mostrar na tela qual dos professores tem salário total maior.

hora1 = int(input("Informe a quantidade de horas aula dada: "))
valor1 = int(input("Informe o valor por hora da aula: "))
salario1 = valor1 * hora1 

hora2 = int(input("Informe a quantidade de horas aula dada: "))
valor2 = int(input("Informe o valor por hora da aula: "))
salario2 = valor2 * hora2 

if salario1 > salario2:
    print("O Professor1 tem salário total maior, seu salário é R$ {} ".format(salario1))
else:
    print("O Professor2 tem salário total maior, seu salário é R$ {} ".format(salario2))

#Faça um algoritmo que leia um número inteiro e mostre uma mensagem indicando se este número é par ou ímpar.

num = int(input("Informe um valor: "))
if num % 2 ==0:
    print("{} é par".format(num))
else:
    print("{} é ímpar".format(num))

#Ler o nome de 2 times e o número de gols marcados na partida. Escrever o nome do vencedor. Caso não haja vencedor deverá ser impressa a palavra EMPATE.

time1 = input("Informe o nome do primeiro time: ")
time2 = input("Informe o nome do segundo time: ")
gols_time1 = input("Informe a quantidade de gols do {}: ".format(time1))
gols_time2 = input("Informe a quantidade de gols do {}: ".format(time2))

if gols_time1 > gols_time2:
    print("{} venceu a partida!".format(time1))
if gols_time2 > gols_time1:
    print("{} venceu a partida!".format(time2))
if gols_time1 == gols_time2:
    print("O jogo terminou empatado")

#Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; Caso contrário, o lucro será de 30%. Entrar com o valor do produto e imprimir o valor da venda.

valor_produto = float(input("Informe o valor do produto: "))
if valor_produto < 20:
    lucro = (valor_produto * 45) / 100
    valor_final = valor_produto + lucro
    print("O valor da venda será R$ {}".format(valor_final))
if valor_produto > 20:
    lucro = (valor_produto * 30) / 100
    valor_final = valor_produto + lucro
    print("O valor da venda será R$ {}".format(valor_final))

#Entrar com um número de 1 a 12 e exibir o mês correspondente.

num_mes = int(input("Informe um número de 1 a 12: "))
if num_mes > 12 or num_mes == 0:
    print("Número inválido")
if num_mes == 1:
    print("O mês é Janeiro")
if num_mes == 2:
    print("O mês é Fevereiro")
if num_mes == 3:
    print("O mês é Março")
if num_mes == 4:
    print("O mês é Abril")
if num_mes == 5:
    print("O mês é Maio")
if num_mes == 6:
    print("O mês é Junho")
if num_mes == 7:
    print("O mês é Julho")
if num_mes == 8:
    print("O mês é Agosto")
if num_mes == 9:
    print("O mês é Setembro")
if num_mes == 10:
    print("O mês é Outubro")
if num_mes == 11:
    print("O mês é Novembro")
if num_mes == 12:
    print("O mês é Dezembro")

