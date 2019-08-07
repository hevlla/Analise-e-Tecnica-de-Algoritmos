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
        for i in range(min(inicial, final), max(inicial, final)+1):
            comparacao(i, maior)
            i += 1
        return max(maior)

while True:
    try:
        inicio, fim = map(int, input().split())
        print(inicio, fim, operacao(inicio, fim))
    except EOFError:
        break
