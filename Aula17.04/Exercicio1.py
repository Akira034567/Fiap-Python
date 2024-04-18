pontos = 0
questao= 1

while questao <= 3:

    resposta = input(f"responda a questao{questao}:")
    if questao == 1 and resposta == "b":
        pontos = pontos + 1

    if questao == 2 and resposta == "a":
        pontos = pontos + 1

    if questao == 3 and resposta == "d":
    pontos = pontos + 1
        questao = questao+1

print(f"O aluno fez {pontos} ponto(s).")

 n = 1
 soma = 0

 while n<=10:

x = float(input(f"Digite o número{n}: "))
  soma = soma + x
#
#  n = n + 1
#  print(f"Soma = {soma:.2f}")
#  print(f"Media = {soma/(n - 1):.2f}.")

'''''Exercicios'''
# meses = 1
#
# dep = float(input(f"Digite o valor do deposito:"))
# juros = float(input(f"Digite o valor dos juros:"))
#
# while meses <= 24:
#     dep += dep*juros/100
#     print(f"O redimento total {dep}:")
#     meses += 1

# meses = 1
#
# dep = float(input(f"Digite o valor do deposito:"))
# juros = float(input(f"Digite o valor dos juros:"))
# aplicação = float(input(f"Digite o valor colocado mensalmente:"))
#
# while meses <= 24:
#     dep += (aplicação + dep)*juros/100
#     print(f"O redimento total {dep}:")
#     meses += 1
