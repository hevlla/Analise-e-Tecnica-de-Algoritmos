def comparacao(operacao):
    if operacao in listados:
        return listados[operacao]
    if operacao <= 1:
        return 1
    if (operacao % 2) == 0:
        valor = operacao / 2
    else:
        valor = 3 * operacao + 1
    listados[operacao] = comparacao(valor) + 1
    return listados[operacao]

def operacao():
    maior = 0
    for i in range(min(inicio,fim), max(inicio, fim) + 1):
        resul = comparacao(i)
        if resul > maior:
            maior = resul
    return maior

listados = {}
while True:
    try:
        inicio, fim = map(int, input().split())
        print(inicio, fim, operacao())
    except EOFError:
        break
