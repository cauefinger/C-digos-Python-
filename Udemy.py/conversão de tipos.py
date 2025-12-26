# conversão de tipos imutáveis e primitivos 
# como o Python é uma linguagem de tipagem forte, devemos sempre converter para que funcione

soma = int("1") + 1

print(soma)
print(type(soma))   

# utilizando uma variável para que o código não precise ter rpetições de --- str("11") ---
str_11 = str("11")
print(str_11 + "b")