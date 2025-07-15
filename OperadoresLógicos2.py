janela = "F"
porta = "F"

alarme = (janela == "A") or (porta == "A")
msg = "O seu alarme está tocando? " + str(alarme)
print(msg)