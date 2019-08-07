def comparacao(operacao, lista):
  contador = 1
  while operacao != 1:
    if (operacao % 2) == 0:
        operacao = operacao / 2
        contador += 1
    else:
        operacao = 3 * operacao + 1
        contador += 1
  lista.append(contador)

def operacao(inicial, final):
    maior = []

    while True:
      if inicial == final:
        comparacao(inicial, maior)
        return max(maior)
        break

      else:
        if final < inicial:
          while inicial != final:
            comparacao(final, maior)
            final += 1
        else:
          while inicial != final:
              comparacao(inicial, maior)
              inicial += 1

entrada = input().split()
inicio = int(entrada[0])
fim = int(entrada[1])
print(inicio, fim, operacao(inicio, fim))
