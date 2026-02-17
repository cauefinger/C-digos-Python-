
# Try - tenta executar o código
# Except - ocorreu algum erro ao tentar executar

# try vai executar um bloco de códigos, caso aconteça algum erro, vamos para o 
# except
numero_str = input("Vou dobrar o número que você digitar: ")

try:
    print("STR:", numero_str)
    numero_float = float(numero_str) # Aqui o código quebra, float tenta converter string
    print ("FLOAT:" , numero_float)
    print (f"O dobro de {numero_str} é: {numero_float * 2}")
except ValueError:
    print("Isso não é um número.")
    