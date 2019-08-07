def operacao(inicial, final):
    contador = 1
    operacao = inicial
    maior = []

    while True:
        if inicial == final:
            while operacao != 1:
                if (operacao % 2) == 0:
                    operacao = operacao / 2
                    contador += 1
                else:
                    operacao = 3 * operacao + 1
                    contador += 1
            maior.append(contador)
            return max(maior)
            break

        else:
            while inicial != final:
                while operacao != 1:
                    if (operacao % 2) == 0:
                        operacao = operacao / 2
                        contador += 1
                    else:
                        operacao = 3 * operacao + 1
                        contador += 1
                maior.append(contador)
                contador = 1
                inicial += 1
                operacao = inicial


entrada = input().split()
inicio = int(entrada[0])
fim = int(entrada[1])
print(inicio, fim, operacao(inicio, fim))
