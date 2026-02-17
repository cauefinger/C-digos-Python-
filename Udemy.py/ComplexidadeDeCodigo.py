# Programa que analisa se carro tomou multa ou não

RADAR_1 = 60 # velocidade maxima
LOCAL_1 = 100 # km localizado do radar
RADAR_RANGE = 1 # alcance do radar

carro_localizacao = 101
velocidade_carro = 61
velocidade_passou = velocidade_carro > RADAR_1
carro_multado = carro_localizacao >= (LOCAL_1 - RADAR_RANGE) and carro_localizacao <= (LOCAL_1 + RADAR_RANGE)

if velocidade_passou:
    print("O carro passou da velocidade no radar 1. ")
if carro_multado and velocidade_passou:
    print("O carro foi multado!")