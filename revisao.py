#Faça um algoritmo que leia dois números e mostre o produto desses números.#

valor1 = float(input("Informe o primeiro valor: "))
valor2 = float(input("Informe o segundo valor: "))
resultado = valor1 * valor2
print ("O produto é: {}" .format(resultado))

#Faça um algoritmo que leia uma certa quantidade de chuva em polegadas e escreva o equivalente em milímetros.#
polegada = float(25.4)
chuva = float(input("Informe a quantidade de chuva em polegadas: "))
conversor_chuva = chuva * polegada
conversor_chuva = round(conversor_chuva)
print("O equivalente em milímetros é: {}".format(conversor_chuva))
 
#Faça um algoritmo que leia o salário bruto mensal de um funcionário, calcule e mostre os valores conforme modelo abaixo:

#Salário Bruto :R$
#(-) IR (15%) :R$
#(-) INSS (11%) :R$
#(-) Sindicato (3%) :R$
#Salário Líquido :R$

sal_bruto = float(input("Informe o salário bruto do funcionário: "))
ir = (sal_bruto * 15) / 100
inss = (sal_bruto * 11) / 100
sindicato = (sal_bruto * 3) / 100
sal_liquido = sal_bruto - (ir + inss + sindicato)
print("Desconto IR: R$",+ir,"\n",
    "Desconto INSS: R$",+inss,"\n",
    "Desconto Sindicato: R$",+sindicato,"\n",
    "Salário Líquido: R$",+ sal_liquido
)
 
#Faça um algoritmo que leia uma temperatura em graus Fahrenheit e converta e mostre em graus Centígrados.

fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
celsius = (fahrenheit - 32) * 5 / 9
celsius = round(celsius,2)
print("A conversão para °C é: ",+celsius)

#O governador acaba de liberar R$ 1.000.000.000,00 para construção de casas populares. Cada casa custa o equivalente a 90 salários mínimos. Faça um algoritmo que leia o valor do salário mínimo e calcule a quantidade de casas que podem ser construídas com o recurso liberado.

sal_minimo = float(input("Informe o valor do salário mínimo: "))
casa = 1000000000 / (sal_minimo * 90) 
casa = round(casa)
print("A quantidade de casa que podem ser construídas é: {}".format(casa))

#Maria quer saber quantos litros de gasolina precisa colocar em seu carro e quanto vai gastar para fazer uma viagem até a casa de sua irmã. Faça um algoritmo que leia:
# • A distância da casa de Maria até sua irmã;
# • O consumo do carro de Maria (KM rodados / litro);
# • O preço da gasolina (litro).
# E mostre as informações que Maria necessita.

distancia = float(input("Informe a distância a ser percorrida: "))
consumo = float (input("Informe o consumo do carro (KM rodados / litro):"))
gasolina = float(input("Informe o preço da gasolina: "))
litros = distancia / consumo 
reais = litros * gasolina 
litros = round(litros,2)
reais = round(reais,2)
print("A quantidade de litros será: {} e o dinheiro gasto será: R$ {}".format(litros, reais))


