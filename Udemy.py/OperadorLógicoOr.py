entrada = input("Digite se você quer [E]ntrar ou [S]air: ")
senha = int(input("Digite a sua senha: "))
senha_permitida = (2006)

if (entrada == "E" or entrada == "e") and senha == senha_permitida:
    print("Você entrou no programa!")
else:
    print("Você saiu do programa!") 

# Curto circuito
print(True or False or 0)
#  Quando operador lógico "OR", a expressão sempre para no Truthy
print(0 or False or 0 or "abc")
# ABC é interpretado como Truthy. 

# if (entrada == "E" or entrada == "e") and senha == senha_permitida:
# o *OR* nesse caso "junta" as duas condições como se fossem uma só. Se o usuário digitar "e" OR "E", funciona.

SENHA = input("Senha: ") or "sem senha"
print (SENHA)