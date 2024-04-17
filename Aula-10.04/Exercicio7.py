nTabuada = int(input("Digite um número para ser mostrada a sua tabuada: "))
nInicio = int(input("Digite um número para ser o início de multiplicação da sua tabuada: "))
nFinal = int(input("Digite um número para ser o final de multiplicação da sua tabuada: "))

while nInicio <= nFinal:
    print(f"{nTabuada} X {nInicio} = {nTabuada * nInicio}")
    nInicio += 1
