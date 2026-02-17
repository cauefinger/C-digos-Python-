# faça um programa que mostre se um carro tomou multa ou não
# nele deve conter a velocidade permitida e a velocidade do carro
# conter a localização do carro e a do radar
# conter o raio de alcance do radar

velocidade_permitida = 80
localizacao_radar = 20
raio_alcance = 1

velocidade_carro = 90
localizacao_carro = 21

ultrapassou_velocidade = velocidade_carro > velocidade_permitida
visao_radar = localizacao_carro >= (localizacao_radar - raio_alcance) and localizacao_carro <= (raio_alcance + localizacao_radar)


if ultrapassou_velocidade:
    print("Ultrapassou a velocidade permitida!")
if visao_radar and ultrapassou_velocidade:
    print("Você foi multado!")



