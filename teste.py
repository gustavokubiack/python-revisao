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
